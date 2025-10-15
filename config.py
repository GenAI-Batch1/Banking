import os

from dotenv import load_dotenv

load_dotenv()

preffered_db=os.getenv("PREFFERED_DB")
transaction_fee= os.getenv("TRANSACTION_FEE")
db_url=""

match preffered_db:
    case "mysql":
        db_url=os.getenv("DB_URL_MYSQL")
    case "oracle":
        db_url=os.getenv("DB_URL_ORACLE")