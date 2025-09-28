from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

__all__ = ["get_settings"] 

class _Settings(BaseSettings): 
    model_config = SettingsConfigDict(env_file=".env")
    mongodb_url: str


@lru_cache()
def get_settings() -> _Settings:
    return _Settings()