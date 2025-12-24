from fastapi import FastAPI
from pydantic import BaseModel
from pipeline import clean_text, word_frequency

app = FastAPI(
    title="Text Cleaning and Analysis Tool",
    version="1.0.0",
    description="API for cleaning and analyzing text data."
)

# --------------------
# Pydantic Models
# --------------------

class AnalysisResult(BaseModel):
    total_words: int
    unique_words: int
    word_frequency: dict

class TextCleaningResponse(BaseModel):
    cleaned_text: str
    analysis: AnalysisResult

# --------------------
# Endpoint
# --------------------

@app.post(
    "/clean-text/",
    response_model=TextCleaningResponse,
    summary="Clean and analyze text",
    tags=["Text Cleaning and Analysis"]
)
async def clean_text_endpoint(text: str):
    tokens = clean_text(text)
    freq = word_frequency(tokens)

    return {
        "cleaned_text": " ".join(tokens),
        "analysis": {
            "total_words": len(tokens),
            "unique_words": len(freq),
            "word_frequency": freq
        }
    }
