from fastapi import APIRouter 
from models.Prompts import Prompts 
from config.db import conn 
from schemas.Prompts import userPrompt, usersPrompts

prompt = APIRouter()

@prompt.get("/")
async def welcome():
    return {"Welcome":"AI Sphere"}

@prompt.get("/view_diagnostics")
async def find_all():
    print(conn.local.user.find())
    print(usersPrompts(conn.local.user.find()))
    return usersPrompts(conn.local.prompt.find()) 

@prompt.post("/perform_diagnostics")
async def insert_prompts(prompt: Prompts):
    conn.local.prompt.insert_one(dict(prompt))
    return usersPrompts(conn.local.prompt.find()) 