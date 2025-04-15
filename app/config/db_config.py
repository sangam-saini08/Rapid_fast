# app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    database_url: str = 'postgresql://postgres:postgres@localhost:5432/rapidfire'

    model_config = SettingsConfigDict(
        env_file=".env",           # Default to .env
        env_file_encoding="utf-8"
    )

@lru_cache()
def get_settings() -> Settings:
    return Settings()
