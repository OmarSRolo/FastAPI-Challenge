import ujson
from pydantic import BaseModel


class BaseDTO(BaseModel):
    class Config:
        orm_mode = True
        json_loads = ujson.loads
        json_dumps = ujson.dumps
