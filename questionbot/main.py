from fastapi import FastAPI
from model.Question import Question
from model.Questionnaire import Questionnaire

app = FastAPI()

# Think about how you would preserve async for image generation
# Fine to leave them as files / files to download,
# But consider unique naming them based on the slack image tag
# And either adding a job or post-process step to cleaning them up
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{questionnaire_id}")
async def read_questionnaire(questionnaire_id: int):
    return {"questionnaire_id": questionnaire_id}

@app.post("/questionnaires/")
async def create_questionnaire(questionnaire: Questionnaire):
    return questionnaire