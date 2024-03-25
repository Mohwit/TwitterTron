import google.generativeai as genai
from dotenv import load_dotenv
import os
import pickle

from prompt import system_prompt

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("models/gemini-pro")
generation_config = genai.GenerationConfig(temperature=0.1, max_output_tokens=4096)

with open("tweets_history.pickle", "rb") as file:
    messages = pickle.load(file)

if len(messages) == 0:
    messages = [{"role": "user", "parts": [system_prompt]}]
    tweet = model.generate_content(messages)
    print(tweet.text)

else:
    messages.append({"role": "user", "parts": ["Provide a new tweet."]})
    tweet = model.generate_content(messages)
    print(tweet.text)

message = messages.append(tweet.candidates[0].content)

with open("tweets_history.pickle", "wb") as file:
    pickle.dump(messages, file)
