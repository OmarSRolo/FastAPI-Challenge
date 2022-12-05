from apps.jokes.dao import JokeDAO
from data_layer.interfaces import IDAO


class JokeService:
    dao: IDAO = JokeDAO()

    async def new_joke(self, joke: str):
        return await self.dao.insert(text=joke)
