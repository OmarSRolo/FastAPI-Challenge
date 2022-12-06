from datetime import datetime

import pytest
from httpx import AsyncClient
from sqlalchemy import select, insert

from data_layer.model import JokeModel
from settings.base import async_database


@pytest.fixture
async def new_joke():
    return await async_database.execute(insert(JokeModel),
                                        values={"created_at": datetime.now(), "is_active": True,
                                                "text": "This is a joke"})


@pytest.mark.anyio
async def test_get_joke_with_none_param_random_result(client: AsyncClient):
    response = await client.get("/api/v1/jokes")
    assert response.status_code == 200


@pytest.mark.anyio
async def test_get_dad_joke(client: AsyncClient):
    response = await client.get("/api/v1/jokes", params={"joke_type": "Dad"})
    assert response.json()["joke"]
    assert response.json()["id"]
    assert response.json()["status"] == 200
    assert response.status_code == 200


@pytest.mark.anyio
async def test_get_wrong_type_joke(client: AsyncClient):
    response = await client.get("/api/v1/jokes", params={"joke_type": "AAA"})
    assert response.status_code == 422


@pytest.mark.anyio
async def test_get_chuck_joke(client: AsyncClient):
    response = await client.get("/api/v1/jokes", params={"joke_type": "Chuck"})
    assert response.json()["value"]
    assert response.json()["id"]
    assert response.json()["url"]
    assert response.status_code == 200


@pytest.mark.anyio
async def test_add_joke(client: AsyncClient):
    response = await client.post("/api/v1/jokes", data={"text": "JOKE JOKE"})
    assert response.json()["text"] == "JOKE JOKE"
    assert response.status_code == 201
    assert await async_database.fetch_one(select(JokeModel.id, JokeModel.text).filter_by(text="JOKE JOKE"))


@pytest.mark.anyio
async def test_update_joke(client: AsyncClient, new_joke: int):
    response = await client.patch("/api/v1/jokes", data={"id": new_joke, "text": "UPDATING"})
    assert response.json() == {"id": new_joke, "text": "UPDATING"}
    assert response.status_code == 200
    joke = await async_database.fetch_one(select(JokeModel.id, JokeModel.text).where(JokeModel.id == new_joke))
    assert joke.text == "UPDATING"


@pytest.mark.anyio
async def test_delete_joke(client: AsyncClient, new_joke: int):
    response = await client.delete("/api/v1/jokes", params={"id": new_joke})
    assert response.json() == {"message": "Joke deleted"}
    assert response.status_code == 200
    joke = await async_database.fetch_one(select(JokeModel).where(JokeModel.id == new_joke))

