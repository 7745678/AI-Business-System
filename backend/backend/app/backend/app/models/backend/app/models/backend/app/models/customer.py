from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime

from app.database import Base


class Customer(Base):
    __tablename__ = "customers"

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

    customer_code = Column(
        String,
        unique=True,
        nullable=True
    )

    name = Column(
        String,
        nullable=False
    )

    phone = Column(
        String,
        nullable=True
    )

    address = Column(
        String,
        nullable=True
    )

    credit_limit = Column(
        Float,
        default=0
    )

    balance = Column(
        Float,
        default=0
    )

    notes = Column(
        String,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
