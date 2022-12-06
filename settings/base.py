from functools import lru_cache
from typing import Final
from data_layer.dbcontext import AlchemyDBContext
import databases

from pydantic import BaseSettings, Field


class SettingsEnviron(BaseSettings):
    CONNECTION_STRING: Final[str] = Field(..., env='CONNECTION_STRING')
    TEST_CONNECTION_STRING: Final[str] = Field(..., env='TEST_CONNECTION_STRING')
    TEST: Final[bool] = Field(..., env='TEST')

    class Config:
        env_prefix = ""
        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache()
def get_settings():
    return SettingsEnviron()


database = AlchemyDBContext(url_connection=get_settings().CONNECTION_STRING)
async_database = databases.Database(
    get_settings().TEST_CONNECTION_STRING if get_settings().TEST else get_settings().CONNECTION_STRING)
