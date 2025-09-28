from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

__all__ = ["get_settings"] 

class _Settings(BaseSettings): 
    app_name: str = "Awesome API"
    items_per_user: int = 50
    mongodb_url: str

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache()
def get_settings() -> _Settings:
    return _Settings()