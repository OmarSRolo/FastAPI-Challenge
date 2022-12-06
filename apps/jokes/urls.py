from fastapi import APIRouter, Depends, status, Query, Form, HTTPException

from apps.jokes.dto import JokeIdDTO
from apps.jokes.enums import TypeJokeEnum
from apps.jokes.factory import JokeFactory
from apps.jokes.service import JokeService

router = APIRouter(prefix="/jokes", tags=["Jokes"])


@router.get("")
async def get_joke(factory: JokeFactory = Depends(), joke_type: TypeJokeEnum | None = Query(default=None)):
    provider = factory.get_data_provider(joke_type)
    joke_from_service = await provider.get_joke()
    return joke_from_service


@router.post("", response_model=JokeIdDTO, status_code=status.HTTP_201_CREATED)
async def add_joke(service: JokeService = Depends(), text: str = Form()):
    id_saved = await service.new_joke(text=text)
    return {"id": id_saved, "text": text}


@router.patch("", response_model=JokeIdDTO, status_code=status.HTTP_200_OK)
async def update_joke(service: JokeService = Depends(), number: int = Form(), text: str = Form()):
    joke_saved = await service.retrieve(id=number)
    if joke_saved is None:
        raise HTTPException(status_code=404, detail="Joke not found")
    await service.update_joke(id=number, text=text)
    return {"id": number, "text": text}


@router.delete("")
async def delete_joke(service: JokeService = Depends(), number: int = Query()):
    joke_saved = await service.retrieve(id=number)
    if joke_saved is None:
        raise HTTPException(status_code=404, detail="Joke not found")
    await service.delete(id=number)
    return {"message": "Joke deleted"}
