#pydantic models

from flask import Flask, requests, jsonify
from pydantic import BaseModel, ValidationError
from ..services.repository_db import AccountRepositoryDB
from ..infra.db import init_db
from ..models.savings import SavingsAccount
from ..models.current import CurrentAccount



app= Flask(__name__)

repo= AccountRepositoryDB()

class CreateAccountDTO(BaseModel):
    account_number: str
    holder_name : str
    type: str #savings, current
    phone: str
    balance: float= 0.0

class AmountDTO(BaseModel):
    amount: float
    remarks: str =""

@app.before_first_request
def setup():
    init_db()

@app.post("/accounts")
def create_accounts():
    try:
      data= CreateAccountDTO(**requests.json)
    except ValidationError as ve:
        return jsonify({"Error": ve.errors()}),400
    account_type=data.type.lower()
    if account_type=="savings":
        acc= SavingsAccount(data.holder_name, data.account_number,data.phone,data.balance)
    elif account_type == "current":
        acc= CurrentAccount(data.holder_name,data.account_number,data.phone,data.balance)
    else:
        return jsonify({"Error": "Invalid type provided"}), 400
    
    repo.add(acc)
    return jsonify({"message":"Account cerated successfully"}),200
    
#getaccount
#withdraw
#deposit
#transfer
#print statement

if __name__ == "__main__":
   app.run(debug=True)

