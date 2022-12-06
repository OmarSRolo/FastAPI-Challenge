from apps.jokes.dao import JokeDAO
from data_layer.interfaces import IDAO


class JokeService:
    dao: IDAO = JokeDAO()

    async def new_joke(self, text: str):
        return await self.dao.insert(text=text)

    async def update_joke(self, id: int, text: str):
        return await self.dao.update(id=id, text=text)

    async def retrieve(self, id: int):
        return await self.dao.retrieve(id=id)

    async def delete(self, id: int):
        return await self.dao.delete(id=id)
