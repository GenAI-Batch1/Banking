from ..models.savings import SavingsAccount
from ..models.current import CurrentAccount

def create_accounts():
    acc1=SavingsAccount("Ravi","sa-001","12345678",105.10)
    acc2=SavingsAccount("Ramesh","sa-002","12345679",150.10)
    acc3=CurrentAccount("Suresh","ca-001","12345688",250.10)
    return [acc1,acc2,acc3]