# The Open AI API gives access to all of Open AI's various LLM's in your application
import os
from dotenv import  load_dotenv
from openai import OpenAI
from pyexpat.errors import messages

load_dotenv()

api_key = os.environ.get("open_ai_api_key")
base_url = os.environ.get("base_url")

client = OpenAI(api_key=api_key, base_url=base_url)


def get_chat_completion(messages):
    return client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1
    )

prompt = "Give a concise explanation of the difference between static arrays and dynamic arrays."
messages = [
    {"role": "system", "content": "You are a ferocious pirate, traversing the seven seas in search of all it's riches."},
    {"role": "user", "content": "What are you?"},
]

chat_completion = get_chat_completion(messages)
gpt_response = chat_completion.choices[0].message.content

print(gpt_response)