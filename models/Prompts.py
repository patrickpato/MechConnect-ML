from pydantic import BaseModel  

class Prompts(BaseModel):
    prompt: str # input from car owner 
    actualIssue: str  # what mechanic states is the problem. 
