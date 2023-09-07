import os
import openai
import sqlite3
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse


OPENAI_API_KEY = ""

openai.api_key = OPENAI_API_KEY

app = FastAPI()

@app.get('/')
async def ping():
    return 'LLM Platform'

@app.api_route("/chat/completions/{model_name}",
               methods=["POST", "OPTIONS"])
async def call_chat_model(model_name: str, request: Request):
    openai_params = await request.json()

    if model_name == 'open-ai':
        openai_response = openai.ChatCompletion.create(
                **openai_params,
            )
        return JSONResponse(content=openai_response)
    else:
        return JSONResponse(content="model not suported")
