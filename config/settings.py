from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    ENV: str = "dev"
    API_BASE_URL: str = "http://localhost:8000"
    
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "testdb"
    POSTGRES_USER: str = "testuser"
    POSTGRES_PASSWORD: str = "testpass"
    
    SQLITE_DB_PATH: str = ":memory:"
    
    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"
    SELENIUM_GRID_URL: str = "http://localhost:4444"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
