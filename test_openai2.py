import os

from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

response = client.responses.create(
    model="gpt-5-nano",
    instructions="You are a coding assistant and optimization expert.",
    input="Provide a basic example in pure python (numpy can be used if required) of a network simplex algorithm being applied.",
)

print(response.output_text)