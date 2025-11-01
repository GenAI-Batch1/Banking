from repository import AccountRepository
from ..infra.db import session_local
from ..infra.orm_models import AccountORM,TransactionORM
from ..infra.mappers import new_tx, to_domain, domain_back
from sqlalchemy import select
from sqlalchemy.orm import joinedload


class AccountRepositoryDB(AccountRepository):

    def __init__(self):
        self._Session = session_local

    def add(self, account ):
        with self._Session as session:
            tp= "savings" if account.__class__.__name__ == "SavingsAccount" else "current"

            acc_orm=AccountORM(account_number=account._account_number,holder_name=account.holder_name,
                type = tp,
                balance= account.get_balance())
            
            session.add(acc_orm)
            #add respective transaction``
            for tr in  account._account_transactions:
                session.add(new_tx(acc_orm,tr["type"],tr["amount"],tr.get("remarks","")))
            session.commit()

#select * from accountorm where account_number="1001"
    def get(self, account_number: str):
        with self._Session as session:
            stmt=select(AccountORM).options(joinedload(AccountORM.transactions)).where(AccountORM.account_number == account_number)
            orm= session.execute(stmt).scalar_one_or_none()
            return to_domain(orm) if orm else None
        
    def all(self):
        with self._Session as session:
            stmt=select(AccountORM).options(joinedload(AccountORM.transactions))
            return [to_domain(orm_obj) for orm_obj in session.execute(stmt).scalars().all()]
            '''
            session_exe=session.execute(stmt).scalars().all()
            transac_list=[]

            for orm_obj in session_exe:
                transac_list.append(to_domain(orm_obj))
                '''

            


        

                