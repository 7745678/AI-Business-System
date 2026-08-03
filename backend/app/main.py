from fastapi import FastAPI

from app.database_init import create_tables
from app.routes.customers import router as customers_router
from app.routes.suppliers import router as suppliers_router
from app.routes.transactions import router as transactions_router

app = FastAPI(
    title="AI Business System",
    description="Smart AI Business Management System",
    version="0.1.0"
)

@app.on_event("startup")
def startup_event():
    create_tables()

app.include_router(customers_router)
app.include_router(suppliers_router)
app.include_router(transactions_router)

@app.get("/")
def root():
    return {"message": "AI Business System is running successfully"}
