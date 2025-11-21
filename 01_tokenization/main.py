import tiktoken

import requests
import json

enc = tiktoken.encoding_for_model("gpt-4o")

text = input("Enter your promt\n") 

tokens =  enc.encode(text)

url = "http://localhost:11434/api/generate"

payload = {
    "model": "phi3",
    "prompt": text,
    "stream": False  
}

response = requests.post(url, json=payload)


data = response.json()

print("Model response:")
print(data["response"])


decode = enc.decode(tokens)

