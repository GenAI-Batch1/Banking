from repository import AccountRepository
from ..infra.db import session_local
from ..infra.orm_models import AccountORM,TransactionORM


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

            #add respective transaction






            
    