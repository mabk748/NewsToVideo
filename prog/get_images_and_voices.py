from dotenv import load_dotenv
import requests
from pathlib import Path
import os

load_dotenv()

class getVoices:
    def __init__(self, text: str, path: Path) -> None:
        self.textToCover = text
        self.voiceDirectory = path
        self.eleven_key = os.getenv["ELEVENLAB_KEY"]
    
    def get_voice(self):
        CHUNK_SIZE = 1024
        # To change voice head to "https://api.elevenlabs.io/v1/voices"
        url = "https://api.elevenlabs.io/v1/text-to-speech/XrExE9yKIg1WjnnlVkGX"

        headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": self.eleven_key
        }

        data = {
        "text": self.textToCover,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
        }

        response = requests.post(url, json=data, headers=headers)
        with open(self.voiceDirectory + 'output.mp3', 'wb') as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    f.write(chunk)


class getImages:
    def __init__(self) -> None:
        pass