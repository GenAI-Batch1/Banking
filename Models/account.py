
from typing import List, Dict

#encapsulation, inheritence, polymorphism, abstraction

class Account():
    bank_name="GenAi Bank"

    def __init__(self,holder_name : str,account_number : str, holder_phone: str,account_balance : float):
        self.holder_name=holder_name
        self.__account_number=account_number
        self.__holder_phone=holder_phone
        self.__account_balance= account_balance
        self.__account_transactions:List[Dict] =[]

    def get_balance(self):
        return self.__account_balance
    
    def depost(self, amount: float, remarks: str):
        self.__account_balance=self.__account_balance + amount
        self.__account_transactions.append({"type":"Deposit", "amount": amount, "remarks": remarks})
