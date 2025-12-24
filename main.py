from fastapi import FastAPI
from pydantic import BaseModel
import re
from collections import Counter

app = FastAPI(
    title="Text Cleaning and Analysis Tool",
    version="1.0.0",
    description="API for cleaning and analyzing text data."
)


def clean_text_util(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

def analyze_text(text: str) -> dict:
    words = text.split()
    return {
        "total_words": len(words),
        "unique_words": len(set(words)),
        "word_frequency": Counter(words)
    }

class AnalysisResult(BaseModel):
    total_words: int
    unique_words: int
    word_frequency: dict

class TextCleaningResponse(BaseModel):
    cleaned_text: str
    analysis: AnalysisResult

@app.post("/clean-text/", response_model=TextCleaningResponse, summary="Clean and analyze text", tags=["Text Cleaning and Analysis"])
async def clean_text_endpoint(Text: str):
    cleaned = clean_text_util(Text)
    analysis = analyze_text(cleaned)

    return {
        "cleaned_text": cleaned,
        "analysis": analysis
    }
