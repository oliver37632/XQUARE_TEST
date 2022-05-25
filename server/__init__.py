from pydantic import BaseSettings

from functools import lru_cache

from datetime import timedelta

from fastapi_jwt_auth import AuthJWT

class Settings(BaseSettings):
    MYSQL_DB_URL: str
    authjwt_secret_key: str
    ALGORITHM: str
    ACCESS_TIMEOUT: timedelta

@AuthJWT.load_config
def get_config():
    return Settings()

@lru_cache()
def get_settings():
    return Settings()