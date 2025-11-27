from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()
client = Client(
    host="http://localhost:11434"
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/chat")
def chat(
    message: str = Body(..., description="The Message")
):
    response = client.chat(model="phi3:mini", messages=[
        {"role": "user", "content": message}

    ])

    return {"response": response.message.content}


# fastapi dev .\server.py
# use above cmdlet to start the fastapi server
