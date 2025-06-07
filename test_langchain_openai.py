from dotenv import load_dotenv

from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model("gpt-4o-mini", model_provider="openai")
print(model.invoke("Hello, world!"))