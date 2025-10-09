from banking.models.account import Account
from typing import Dict,Optional

'''
Add acoounts,
get account by account number
read all accounts 
'''

class AccountService:
    def __init__(self):
        self._store: Dict[str,Account] ={}

    def add_account(self, account : Account) -> None:
        self._store[account._acount_number] = account

    def get_account(self,account_number):
        return self._store.get(account_number)
    

    def get_all_accounts(self):
        return self._store.values()