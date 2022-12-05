from fastapi import APIRouter, Depends, status, Query, Form

from apps.jokes.dto import JokeIdDTO
from apps.jokes.enums import TypeJokeEnum
from apps.jokes.factory import JokeFactory
from apps.jokes.service import JokeService

router = APIRouter(prefix="/jokes", tags=["Jokes"])


@router.get("")
async def get_joke(factory: JokeFactory = Depends(), joke_type: TypeJokeEnum | None = Query(default=None)):
    provider = factory.get_data_provider(joke_type)
    print(joke_type)
    return await provider.get_joke()


@router.post("", response_model=JokeIdDTO, status_code=status.HTTP_201_CREATED)
async def add_joke(service: JokeService = Depends(), joke: str = Form()):
    _id = await service.new_joke(joke=joke)
    return {"id": _id, "joke": joke}


@router.patch("")
async def update_joke():
    return ""


@router.delete("")
async def delete_joke():
    return ""
