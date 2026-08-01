from sqlalchemy import Column, Integer, Float, String, ForeignKey

from app.database import Base


class InvoiceItem(Base):
    __tablename__ = "invoice_items"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    invoice_id = Column(
        Integer,
        ForeignKey("invoices.id"),
        nullable=False
    )

    product_name = Column(
        String,
        nullable=False
    )

    quantity = Column(
        Float,
        default=1
    )

    unit_price = Column(
        Float,
        default=0
    )

    total_price = Column(
        Float,
        default=0
    )
