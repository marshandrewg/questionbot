from pydantic import BaseModel

class Choice(BaseModel):
    id: str
    text: str

class Question(BaseModel):
    id: str
    text: str
    tags: list[str]
    initial_weight: int
    choices: list[Choice]
    correct_choice_ids: list[str]