from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from datetime import datetime

from app.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    company_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=False
    )

    customer_id = Column(
        Integer,
        ForeignKey("customers.id"),
        nullable=True
    )

    supplier_id = Column(
        Integer,
        ForeignKey("suppliers.id"),
        nullable=True
    )

    amount = Column(
        Float,
        nullable=False
    )

    payment_type = Column(
        String,
        nullable=False
    )

    payment_method = Column(
        String,
        default="CASH"
    )

    reference_number = Column(
        String,
        nullable=True
    )

    notes = Column(
        String,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
