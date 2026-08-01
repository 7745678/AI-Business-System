from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.supplier import Supplier


router = APIRouter(
    prefix="/suppliers",
    tags=["Suppliers"]
)


@router.post("/")
def create_supplier(
    name: str,
    phone: str = None,
    db: Session = Depends(get_db)
):
    supplier = Supplier(
        company_id=1,
        name=name,
        phone=phone
    )

    db.add(supplier)
    db.commit()
    db.refresh(supplier)

    return supplier


@router.get("/")
def get_suppliers(
    db: Session = Depends(get_db)
):
    return db.query(Supplier).all()
