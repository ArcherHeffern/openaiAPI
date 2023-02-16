There are 3 parts to getting this working
1. Get an API Key from OpenAI
2. Put the API Key in a .env file
3. Activate the virtual enviroment

1. 
    Go to https://platform.openai.com/account/api-keys, create an account if you haven't. Then create a new private key and copy it
2. Create a file named .env
    write in it: API_KEY="yourAPIKEY"
    NOTE: There cannot be any spaces
3. type in your VSCode terminal:
    source venv/bin/activate

Now you can run this as python openaiapi.py

Once your done, write: deactivate