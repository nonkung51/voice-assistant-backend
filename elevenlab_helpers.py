from io import BytesIO
import os
import requests

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

ELEVENLABS_API_KEY  = os.getenv('ELEVENLABS_API_KEY')
ELEVENLABS_VOICE_ID  = os.getenv('ELEVENLABS_VOICE_ID')

url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}"

headers = {
  "content-type": "application/json",
  "accept": "audio/mpeg",
  "xi-api-key": ELEVENLABS_API_KEY
}

def get_TTS(text="Hello My name is Harry"):
    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }
    audio_data = requests.request("POST", url, json=payload, headers=headers)
    
    buffer = BytesIO()

    for chunk in audio_data.iter_content(chunk_size=1024):
        if chunk:
            buffer.write(chunk)
    buffer.seek(0)

    return iter(buffer.read, b"")