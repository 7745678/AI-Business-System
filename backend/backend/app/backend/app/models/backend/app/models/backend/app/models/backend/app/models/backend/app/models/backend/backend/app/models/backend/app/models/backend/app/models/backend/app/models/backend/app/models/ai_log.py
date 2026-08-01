from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from datetime import datetime

from app.database import Base


class AILog(Base):
    __tablename__ = "ai_logs"

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

    input_text = Column(
        Text,
        nullable=False
    )

    ai_action = Column(
        String,
        nullable=True
    )

    ai_result = Column(
        Text,
        nullable=True
    )

    confidence = Column(
        String,
        nullable=True
    )

    status = Column(
        String,
        default="PENDING"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
