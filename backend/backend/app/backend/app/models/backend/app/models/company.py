from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)

    company_name = Column(
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

    currency = Column(
        String,
        default="YER"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
