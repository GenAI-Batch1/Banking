from ..services.account_service import AccountService
from ..app.seed import create_accounts
from ..services.ledger import LedgerService


def run_demo():
    acc_service = AccountService() 

    for acc in create_accounts():
        acc_service.add_account(acc)

    
    a1=acc_service.get_account("sa-001")
    a2=acc_service.get_account("sa-002")
    a3=acc_service.get_account("ca-001")
    

    a1.deposit(20,"cash deposit")
    a2.widthdraw(5,"Cash widthdrawl")

    LedgerService.amount_transfer(a1,a2,10)

    #LedgerService.print_statement(a1,3)
    LedgerService.print_statement(a2,5)


if __name__ == "__main__":
    run_demo()