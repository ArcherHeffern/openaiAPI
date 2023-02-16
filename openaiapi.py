import os
import sys
import openai
from dotenv import load_dotenv

load_dotenv()

# Set up the OpenAI API client
# get api key at: https://platform.openai.com/account/api-keys
openai.api_key = os.getenv('API_KEY')

# test for an API key
if openai.api_key=="YOUR_API_KEY":
    print("You need to get an openapi api key to use this demo")
    sys.exit()

# Set up the model and prompt
MODEL_ENGINE = "text-davinci-003"
prompt = input("Enter a prompt: ")

# Generate a response
completion = openai.Completion.create(
    engine=MODEL_ENGINE,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)
