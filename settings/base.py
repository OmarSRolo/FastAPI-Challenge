from functools import lru_cache
from typing import Final

from pydantic import BaseSettings


class SettingsEnviron(BaseSettings):
    CONNECTION_STRING: Final[str]
    TEST_CONNECTION_STRING: Final[str]
    TEST: Final[bool]

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache()
def get_settings():
    return SettingsEnviron()
