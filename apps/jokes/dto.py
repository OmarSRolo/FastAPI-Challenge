from system.dto import BaseDTO


class JokeDTO(BaseDTO):
    joke: str


class JokeIdDTO(BaseDTO):
    id: int
    joke: str
