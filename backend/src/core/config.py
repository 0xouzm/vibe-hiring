from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "./data/talentdrop.db"
    jwt_secret: str = "demo-secret-key"
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 1440  # 24 hours

    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"
    openai_embedding_model: str = "text-embedding-3-large"

    lightrag_working_dir: str = "./data/lightrag"

    log_dir: str = "./logs"

    model_config = {"env_file": ".env", "extra": "ignore"}


settings = Settings()
