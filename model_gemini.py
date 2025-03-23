import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
import os

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key = api_key)

models = genai.list_models()
for model in models:
    print(f"Model: {model.name} - Supported Methods: {model.supported_generation_methods}")
