from fastapi import APIRouter, Depends, status, Body, Query

from apps.jokes.dto import JokeIdDTO
from apps.jokes.enums import TypeJokeEnum
from apps.jokes.service import JokeService

router = APIRouter(prefix="/jokes", tags=["Jokes"])


@router.get("")
async def get_joke(service: JokeService = Depends(), provider: TypeJokeEnum | None = Query(default=None)):
    return ""


@router.post("", response_model=JokeIdDTO, status_code=status.HTTP_201_CREATED)
async def add_joke(service: JokeService = Depends(), body: dict = Body()):
    _id = await service.new_joke(**body)
    return {"id": _id, "joke": body["joke"]}


@router.patch("")
async def update_joke():
    return ""


@router.delete("")
async def delete_joke():
    return ""
