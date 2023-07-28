# uvicorn main:app --reload

from fastapi import FastAPI
from typing import List, Dict
from pydantic import BaseModel

app = FastAPI()

class Conversation(BaseModel):
    role: str
    content: str

class Payload(BaseModel):
    conversation: List[Conversation]
    scenario: str

@app.post("/conversation/")
async def process_conversation(payload: Payload) -> Dict[str, str]:
    # Process conversation here
    print(payload)
    response = {"message": "Conversation processed successfully!"}
    
    return response