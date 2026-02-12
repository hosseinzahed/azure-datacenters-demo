from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "az_dc_db"
    db_user: str = "postgres"
    db_password: str = "postgres"

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
