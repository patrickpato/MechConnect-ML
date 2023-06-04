from fastapi import FastAPI 
from routes.Prompts import prompt

app = FastAPI() 
app.include_router(prompt)
