from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    KLIKINDOMART_BASE_URL: str
    KLIKINDOMART_PARAMS: str
    KLIKINDOMART_PARAM_PAGE: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
