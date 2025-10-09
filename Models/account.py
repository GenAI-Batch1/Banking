
from typing import List, Dict
from abc import ABC, abstractmethod

#encapsulation, inheritence, polymorphism, abstraction

class Account():
    bank_name="GenAi Bank"

    def __init__(self,holder_name : str,account_number : str, holder_phone: str,account_balance : float):
        self.holder_name=holder_name
        self._account_number=account_number
        self.__holder_phone=holder_phone
        self.__account_balance= account_balance
        self._account_transactions:List[Dict] =[]

    def get_balance(self):
        return self.__account_balance
    
    def set_balance(self, updated_balance):
        self.__account_balance=updated_balance
    
    def deposit(self, amount: float, remarks: str = "deposit"):
        self.__account_balance=self.__account_balance + amount
        self._account_transactions.append({"type":"Deposit", "amount": amount, "remarks": remarks})
        
    def mini_statement(self, last_n : int=5) -> List[Dict]:
        return self._account_transactions[-1:-last_n]
    

    @abstractmethod
    def widthdraw(self, amount: float, remarks: str ="widthdrawl"):