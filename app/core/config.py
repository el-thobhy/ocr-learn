from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_path: str = "./model"
    env: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()