import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Select model and temperature (you can adjust this)
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize the chat session
chat = model.start_chat(history=[])

# Optional: Allow user to set temperature
try:
    temp = float(input("Set temperature (e.g., 0.7 for balanced creativity): "))
except:
    print("Invalid input. Using default temperature of 0.7.")
    temp = 0.7

print("\nGemini Chat Started. Type your messages.\n")

# Multi-turn conversation
for i in range(3):  # 3-turn conversation (can increase)
    user_input = input(f"User [{i+1}]: ")
    response = chat.send_message(user_input, generation_config={"temperature": temp})
    print(f"\nGemini [{i+1}]: {response.text}\n")

print("✅ Final Gemini Response (above). Chat ended.")
