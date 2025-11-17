import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env file
load_dotenv()

# Configure with API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create model object
model = genai.GenerativeModel("gemini-2.0-flash")

def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    user_input = input("You: ")
    reply = ask_gemini(user_input)
    print("AI:", reply)
