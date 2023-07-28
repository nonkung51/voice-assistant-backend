# uvicorn main:app --reload

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from typing import List, Dict
from pydantic import BaseModel

from openai_helpers import get_completion_from_messages
from elevenlab_helpers import get_TTS

app = FastAPI()

class Conversation(BaseModel):
    role: str
    content: str

class Payload(BaseModel):
    conversation: List[Conversation]
    scenario: str

@app.post("/conversation/")
async def process_conversation(payload: Payload):
    # Prepare data
    req_payload = payload.dict()
    conversation = req_payload.get("conversation", [])
    scenario = req_payload.get("scenario", "default")
    
    # ChatGPT API
    message = get_completion_from_messages(conversation, model="gpt-3.5-turbo", temperature=0)
    
    # ElevenLab API
    audio_data = get_TTS(message)
    
    return StreamingResponse(audio_data, media_type="audio/mpeg")