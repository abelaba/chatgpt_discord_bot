import openai
import os

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatGPT:
    
    def getOpenAIResponse(self, text: str):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=text,
            temperature=0.8,
            max_tokens=800,
        )
        return response.choices[0].text
