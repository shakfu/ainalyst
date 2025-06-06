import os

from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()  # take environment variables


client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)

message = client.messages.create(
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Hello, Claude. When is dark matter?",
        }
    ],
    model="claude-3-5-haiku-latest",
)
print(message.content)
