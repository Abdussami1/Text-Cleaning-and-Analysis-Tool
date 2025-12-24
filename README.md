# Text Cleaning and Analysis Tool

A FastAPI-based API for cleaning text and performing basic text analysis, useful for AI/ML and NLP preprocessing tasks.

---

## 🚀 Features
- Remove special characters and punctuation
- Tokenize text into words
- Normalize text (lowercasing & trimming)
- Remove empty tokens
- Count total words
- Count unique words
- Generate word frequency statistics
- Modular text-processing pipeline
- Auto-generated API documentation (Swagger & ReDoc)

---

## 🛠 Tech Stack
- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn

---
## 📁 Project Structure

```text
.
├── main.py          # FastAPI application
├── pipeline.py      # Text cleaning & processing pipeline
├── requirements.txt
├── README.md
```

---

## 📡 API Endpoint

### `POST /clean-text/`

Cleans the input text and returns analysis results.

### Request Body

```json
{
  "text": "AI will change the world! AI is powerful."
}
```


### Example Responce

```json
{
  "cleaned_text": "ai will change the world ai is powerful",
  "analysis": {
    "total_words": 8,
    "unique_words": 7,
    "word_frequency": {
      "ai": 2,
      "will": 1,
      "change": 1,
      "the": 1,
      "world": 1,
      "is": 1,
      "powerful": 1
    }
  }
}
```

### ▶️ How to Run

# Create virtual environment (optional)
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate   # Windows
# source .venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn main:app --reload

