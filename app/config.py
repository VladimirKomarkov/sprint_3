from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    rabbitmq_url: str = "amqp://quest:guest@localhost:5672/"

    database_url: str = "postgresql+psycopg2://owner:password@localhost:5432/jip_project"

    class Config:
        env_file = ".env"


settings = Settings()
