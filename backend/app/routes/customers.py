from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.customer import Customer


router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.post("/")
def create_customer(
    name: str,
    phone: str = None,
    db: Session = Depends(get_db)
):
    customer = Customer(
        company_id=1,
        name=name,
        phone=phone
    )

    db.add(customer)
    db.commit()
    db.refresh(customer)

    return customer


@router.get("/")
def get_customers(
    db: Session = Depends(get_db)
):
    return db.query(Customer).all()
