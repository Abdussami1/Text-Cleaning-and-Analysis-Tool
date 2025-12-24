from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.post("/health")
def health_check():
    return {"status": "ok"}