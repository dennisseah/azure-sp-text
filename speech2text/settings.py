from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    spx_subscription_key: str
    spx_region: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
