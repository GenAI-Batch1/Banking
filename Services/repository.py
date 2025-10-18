from ..models.account import Account
from typing import List

class AccountRepository:
    def add(self, account: Account): 
        pass

    def get(self,acc_number: str) -> Account:
        pass

    def all(self) -> List[Account]:
        pass