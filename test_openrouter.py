import os

from dotenv import load_dotenv
from openrouter import OpenRouter

load_dotenv()

with OpenRouter(api_key=os.getenv("OPENROUTER_API_KEY")) as client:
    response = client.chat.send(
        model="deepseek/deepseek-v4-flash",
        messages=[
            {"role": "user", "content": "What were the causes of the French Revolution?"}
        ],
    )

    print(response.choices[0].message.content)
