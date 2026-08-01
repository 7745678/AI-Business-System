from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    APP_NAME: str = "AI Accounting ERP"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    DATABASE_URL: str = "sqlite:///./ai_accounting.db"

    SECRET_KEY: str = "CHANGE_THIS_SECRET_KEY"

    OPENAI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""
    GOOGLE_API_KEY: str = ""

    WHATSAPP_API_URL: str = ""
    WHATSAPP_ACCESS_TOKEN: str = ""

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
