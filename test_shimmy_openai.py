from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:11435/v1",
    api_key="sk-local"
)

resp = client.chat.completions.create(
    model="gemma-3-4b-it-qat-q4-0",
    messages=[{"role": "user", "content": "Say hi in 5 words."}],
    max_tokens=32,
)

print(resp.choices[0].message.content)
