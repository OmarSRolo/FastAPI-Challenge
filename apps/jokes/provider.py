from httpx import AsyncClient

from data_layer.interfaces import IDataProvider


class ChuckDataProvider(IDataProvider):
    client = AsyncClient(base_url="https://api.chucknorris.io/jokes/random", headers={"Accept": "application/json"})

    async def get_joke(self):
        response = await self.client.get("")
        return response.json()


class CanDataProvider(IDataProvider):
    client = AsyncClient(base_url="https://icanhazdadjoke.com", headers={"Accept": "application/json"})

    async def get_joke(self):
        response = await self.client.get("")
        return response.json()
