'''
amount transfer
print statement on passbook
'''

from banking.models.account import Account

class LedgerService:

    @staticmethod
    def amount_transfer(src_account: Account,dest_account : Account, amount: float):
        src_account.widthdraw(amount,f"Transferd the amount to {dest_account._account_number}")
        dest_account.deposit(amount,f"Deposited the amount from {src_account._account_number}")


    @staticmethod
    def print_statement(account: Account,last_n : int =5):
        #home work
        #print stament
        #print current balance