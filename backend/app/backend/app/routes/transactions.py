from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.transaction import Transaction


router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)


@router.post("/")
def create_transaction(
    company_id: int,
    amount: float,
    transaction_type: str,
    customer_id: int = None,
    supplier_id: int = None,
    description: str = None,
    db: Session = Depends(get_db)
):

    transaction = Transaction(
        company_id=company_id,
        customer_id=customer_id,
        supplier_id=supplier_id,
        amount=amount,
        transaction_type=transaction_type,
        description=description
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction


@router.get("/")
def get_transactions(
    db: Session = Depends(get_db)
):
    return db.query(Transaction).all()
