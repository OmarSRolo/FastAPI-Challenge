from abc import ABC, abstractmethod
from httpx import AsyncClient


class IDAO(ABC):
    model = None

    @abstractmethod
    async def retrieve(self, **kwargs):
        ...

    @abstractmethod
    async def insert(self, **kwargs):
        ...

    @abstractmethod
    async def delete(self, **kwargs):
        ...

    @abstractmethod
    async def update(self, **kwargs):
        ...


class IDataProvider(ABC):
    client = AsyncClient

    @abstractmethod
    async def retrieve(self, **kwargs):
        ...

    @abstractmethod
    async def insert(self, **kwargs):
        ...

    @abstractmethod
    async def delete(self, **kwargs):
        ...

    @abstractmethod
    async def update(self, **kwargs):
        ...
