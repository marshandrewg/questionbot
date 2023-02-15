from fastapi import FastAPI
from model.Question import Question
from model.Questionnaire import Questionnaire

import logging
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

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

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
	exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
	logging.error(f"{request}: {exc_str}")
	content = {'status_code': 10422, 'message': exc_str, 'data': None}
	return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)