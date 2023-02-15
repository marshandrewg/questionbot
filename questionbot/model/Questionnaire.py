from pydantic import BaseModel
from model.Question import Question

class Questionnaire(BaseModel):
    id: str
    text: str
    questions: list[Question]
    tags: list[str]