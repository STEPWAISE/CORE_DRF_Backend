# ENGINE

from dotenv import load_dotenv
import os
import google.generativeai as ggi

# Load the environment variables from the .env file
load_dotenv()

# Fetch the API key from the environment variable
fetched_api_key = os.getenv("GEMINI_KEY")

# Configure the generative AI with the fetched API key
ggi.configure(api_key=fetched_api_key)

def initialize_model():
    model = ggi.GenerativeModel("gemini-pro")
    chat = model.start_chat()
    return chat

gpt = initialize_model()

response = gpt.send_message("Hi How are you?", stream=True)
print(response)