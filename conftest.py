import pytest
from httpx import AsyncClient
from sqlalchemy import create_engine

from data_layer.dbcontext import Base
from server import app
from settings.base import get_settings, async_database


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope='function', autouse=True)
async def db():
    try:
        yield await async_database.connect()
    finally:
        await async_database.disconnect()


@pytest.fixture(scope="function", autouse=True)
async def session():
    engine = create_engine(get_settings().TEST_CONNECTION_STRING)
    try:
        yield Base.metadata.create_all(bind=engine)
    finally:
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="session")
async def client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
