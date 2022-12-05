from datetime import datetime

from sqlalchemy import select, insert, update, delete

from data_layer.interfaces import IDAO
from data_layer.model import JokeModel
from settings.dev import async_database


class JokeDAO(IDAO):
    model = JokeModel

    async def retrieve(self, **kwargs):
        return await async_database.fetch_one(select(self.model).filter_by(is_active=False, **kwargs))

    async def insert(self, **kwargs):
        kwargs["is_active"] = True
        kwargs["created_at"] = datetime.now()
        return await async_database.execute(insert(self.model), values=kwargs)

    async def delete(self, **kwargs):
        await async_database.execute(delete(self.model).filter_by(**{"id": kwargs["id"]}))

    async def update(self, **kwargs):
        await async_database.execute(update(self.model).filter_by(**{"id": kwargs["id"]}).values(**kwargs))
