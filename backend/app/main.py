from fastapi import FastAPI

from app.database_init import create_tables
from app.routes.customers import router as customers_router


app = FastAPI(
    title="AI Accounting ERP",
    description="Smart accounting system for merchants and distributors",
    version="0.1.0"
)


@app.on_event("startup")
def startup_event():
    create_tables()


app.include_router(customers_router)


@app.get("/")
def home():
    return {
        "message": "AI Accounting ERP is running",
        "version": "0.1.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }
