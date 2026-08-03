from app.db.session import engine
from app.models.base import Base

# استيراد جميع النماذج حتى يتم تسجيلها في SQLAlchemy
from app.models.company import Company
from app.models.customer import Customer
from app.models.supplier import Supplier
from app.models.transaction import Transaction
from app.models.invoice import Invoice
from app.models.invoice_item import InvoiceItem
from app.models.payment import Payment
from app.models.file import File
from app.models.whatsapp_message import WhatsAppMessage
from app.models.ai_log import AILog
from app.models.user import User


def create_tables():
    Base.metadata.create_all(bind=engine)
