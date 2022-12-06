import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_api_common_multiple_two_simple_numbers(client: AsyncClient):
    response = await client.get("/api/v1/calc/common_multiple", params={"numbers": [2, 4]})
    assert response.json() == {'result': 4.0}
    assert response.status_code == 200


@pytest.mark.anyio
async def test_api_common_multiple_two_numbers(client: AsyncClient):
    response = await client.get("/api/v1/calc/common_multiple", params={"numbers": [3, 40]})
    assert response.json() == {'result': 120}
    assert response.status_code == 200


@pytest.mark.anyio
async def test_api_common_multiple_many_numbers(client: AsyncClient):
    response = await client.get("/api/v1/calc/common_multiple", params={"numbers": [3, 40, 3, 5, 6, 21, 54]})
    assert response.json() == {'result': 7560}
    assert response.status_code == 200


@pytest.mark.anyio
async def test_api_get_increase_number(client: AsyncClient):
    response = await client.get("/api/v1/calc/add", params={"number": 15})
    assert response.json() == {"next": 16}
    assert response.status_code == 200
