from fastapi import FastAPI

app = FastAPI(
    title="AI Accounting ERP",
    description="Smart accounting system for merchants and distributors",
    version="0.1.0"
)


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
