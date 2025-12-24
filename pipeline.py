import re
from collections import Counter

def tokenize(text: str) -> list:
    return text.split()

def normalize(tokens: list) -> list:
    return [token.lower().strip() for token in tokens]

def remove_empty(tokens: list) -> list:
    return [token for token in tokens if token]

def word_frequency(tokens: list) -> dict:
    return Counter(tokens)

def clean_text(text: str) -> list:
    # Remove non-alphabetic characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    tokens = tokenize(text)
    tokens = normalize(tokens)
    tokens = remove_empty(tokens)

    return tokens
