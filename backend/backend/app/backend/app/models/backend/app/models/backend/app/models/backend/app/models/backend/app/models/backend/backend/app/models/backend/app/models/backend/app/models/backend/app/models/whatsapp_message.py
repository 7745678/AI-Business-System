from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from datetime import datetime

from app.database import Base


class WhatsAppMessage(Base):
    __tablename__ = "whatsapp_messages"

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

    phone_number = Column(
        String,
        nullable=False
    )

    message_text = Column(
        Text,
        nullable=True
    )

    ai_response = Column(
        Text,
        nullable=True
    )

    message_type = Column(
        String,
        nullable=True
    )

    is_processed = Column(
        String,
        default="NO"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
