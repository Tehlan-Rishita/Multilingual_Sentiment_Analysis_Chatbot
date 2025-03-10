import nltk
import spacy
import re

# Download necessary resources
nltk.download('stopwords')

# Load English NLP model for tokenization
nlp = spacy.blank("en")

def clean_text(text):
    """Removes special characters, extra spaces, and normalizes text."""
    text = text.lower().strip()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove special characters
    return text

def preprocess_text(text, language):
    """
    Processes text: cleans, and tokenizes.
    Expects the detected language as input.
    """
    cleaned_text = clean_text(text)
    
    # Tokenization
    doc = nlp(cleaned_text)
    tokens = [token.text for token in doc]

    return {
        "original_text": text,
        "language": language,
        "cleaned_text": cleaned_text,
        "tokens": tokens
    }
