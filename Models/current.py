from .account import Account

class CurrentAccount(Account):
    Transaction_Fee=50

    def widthdraw(self, amount, remarks = "widthdrawl"):
        account_balance=self.get_balance()
        if account_balance > amount + self.Transaction_Fee:
            #disburse amount
            new_balance=account_balance- (amount + self.Transaction_Fee)
            self._account_transactions.append({"type":"Widthdrawl", "amount": amount, "remarks": remarks})
            self._account_transactions.append({"type":"Widthdrawl", "amount": self.Transaction_Fee, "remarks": "Transaction fee for Widthdrawl"})
            self.set_balance(new_balance)
        else:
            return "Insufficient Funds"
