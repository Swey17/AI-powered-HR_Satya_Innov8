from groq import Groq
from dotenv import load_dotenv
import os

# Load GROQ_API_KEY from .env file
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": ""
        },
        {
            "role": "user",
            "content": "",
        }
    ],

    # The language model which will generate the completion.
    model="llama-3.3-70b-versatile"
)

print(chat_completion.choices[0].message.content)