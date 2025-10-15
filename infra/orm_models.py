from db import Base
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import String,Integer, Float, ForeignKey


class AccountORM(Base):
    __tablename__ = "accounts"
    id : Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    account_number: Mapped[str] =mapped_column(String(50), unique=True, index=True)
    holder_name: Mapped[str] =mapped_column(String(50))
    type: Mapped[str] = mapped_column(String(20)) #savings, current
    balance: Mapped[float] =mapped_column(Float,default=0.0)
   

    transactions : Mapped[list["TransactionORM"]]= relationship("TransactionORM",back_populates="accounts")


class TransactionORM(Base):
    __tablename__ = "transactions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    account_id: Mapped[int] =mapped_column(ForeignKey("accounts.id"))
    type: Mapped[str] = mapped_column(String(50)) #deposit, widthdrawl, transctionFee, transfer
    amount : Mapped[float] = mapped_column(Float)
    remarks: Mapped[str] =mapped_column(String(250),default="")

    account: Mapped[AccountORM] = relationship("AccountORM",back_populates="transactions")


