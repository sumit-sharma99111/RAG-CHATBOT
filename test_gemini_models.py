from dotenv import load_dotenv
import google.generativeai as genai
import os

# ✅ Load .env file variables
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

print("🔍 Available Gemini models for your API key:\n")
for m in genai.list_models():
    print("•", m.name)
