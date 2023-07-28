# uvicorn main:app --reload

from fastapi import FastAPI
from fastapi.responses import Response
from typing import List, Dict
from pydantic import BaseModel

from openai_helpers import get_completion_from_messages
from elevenlab_helpers import get_TTS
from prompt_helpers import (outbound_appointment_reminder_scenario, 
                            outbound_appointment_reminder_summarizer)

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
    if scenario == "outbound/appointment-reminder":
        conversation = outbound_appointment_reminder_scenario(conversation)
    else:
        conversation = outbound_appointment_reminder_scenario(conversation)

    message = get_completion_from_messages(conversation, model="gpt-3.5-turbo", temperature=0)  
    summarizer_messages = conversation.copy()

    if scenario == "outbound/appointment-reminder":
        summarizer_messages = outbound_appointment_reminder_summarizer(summarizer_messages)
    else:
        summarizer_messages = outbound_appointment_reminder_summarizer(conversation)
    
    summarizer_result = get_completion_from_messages(summarizer_messages, model="gpt-3.5-turbo", temperature=0)
    
    # ElevenLab API
    audio_data = get_TTS(message)

    # Return response
    headers={"message": message, "conversation-summary": summarizer_result.replace('\n', '')}
    return Response(content=audio_data, headers=headers, media_type="audio/mpeg")