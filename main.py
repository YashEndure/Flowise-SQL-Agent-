from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

FLOWISE_API = "http://localhost:3000/chatbot/ad6ebe01-7cb0-47a7-a6df-49ecca6c10d0"  #Flowise endpoint

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    question = data.get("question", "")

    try:
        response = requests.post(FLOWISE_API, json={"question": question})
        return {"answer": response.json()}
    except Exception as e:
        return {"error": str(e)}
