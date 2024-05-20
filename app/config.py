from pydantic import validator, root_validator, model_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL(self):
        DATABASE_URL: str = f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return DATABASE_URL

    class Config:
        env_file = 'C://Users//tliso//PycharmProjects//ai_detection_app//.env'

settings = Settings()