from orm_models import AccountORM,TransactionORM
from ..models.account import Account
from ..models.savings import SavingsAccount
from ..models.current import CurrentAccount


def to_domain(acc: AccountORM):
    account= ""
    if acc.type == "savings":
        account= SavingsAccount(acc.holder_name,acc.account_number,"",acc.balance)
    elif acc.type == "current":
        account = CurrentAccount(acc.holder_name,acc.account_number,"",acc.balance)
    else:
        return account
    
    for t in acc.transactions:
        account._account_transactions.append({"type":t.type, "amount": t.amount, "remarks": t.remarks})
    return account


def new_tx(account_orm: AccountORM, tx_type: str,amount: float, remarks: str ="") -> TransactionORM:
    return TransactionORM(account= account_orm,type=tx_type, amount=amount, remarks=remarks)

def domain_back(acc_orm: AccountORM, acc: Account):
    acc_orm.holder_name=acc.holder_name
    acc_orm.balance=acc.get_balance()





