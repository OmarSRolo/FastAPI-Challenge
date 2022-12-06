from data_layer.dto import BaseDTO


class JokeDTO(BaseDTO):
    text: str


class JokeIdDTO(BaseDTO):
    id: int
    text: str
