"""
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
from config import SUPPORTED_LANGUAGES

# Ensuring consistent results
DetectorFactory.seed = 42  

def detect_language(text):
    ''''''
    Detects the language of the given text using langdetect.
    Returns the detected language code (ISO 639-1) or 'unknown' if detection fails.
    '''''
    try:
        lang_code = detect(text)
        return lang_code if lang_code in SUPPORTED_LANGUAGES else "unsupported"
    except LangDetectException:
        return "unknown"
"""
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

DetectorFactory.seed = 0  # Ensures consistent detection results

def detect_language(text):
    """Detects the language of the input text and returns structured output."""
    try:
        detected_lang = detect(text)
        return {"language": detected_lang, "text": text}
    except LangDetectException:
        return {"language": "unknown", "text": text}
