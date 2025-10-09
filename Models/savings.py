from .account import Account

class SavingsAccount(Account):

    def widthdraw(self, amount, remarks = "widthdrawl") :
        account_balance = self.get_balance()
        if(account_balance > amount):
            new_balance = account_balance - amount
            self._account_transactions.append({"type":"Widthdrawl", "amount": amount, "remarks": remarks})
            self.set_balance(new_balance)
            return True , "Transaction successfull"
        else:
            return False, "Insufficient Funds"