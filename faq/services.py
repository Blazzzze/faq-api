from django.core.cache import cache
from googletrans import Translator

# Initialize the translator object for use in translations
translator = Translator()


def translate_text(text, lang):
    """
    Translates the given text into the specified language using Google Translate API.

    Args:
        text (str): The text to be translated.
        lang (str): The target language code (e.g., 'hi' for Hindi, 'bn' for Bengali).

    Returns:
        str: The translated text, or the original text if translation fails.
    """
    try:
        # Attempt to translate the text
        return translator.translate(text, dest=lang).text
    except Exception:
        # Return the original text if translation fails
        return text


def get_cached_translation(faq, lang):
    """
    Retrieves the translation of the FAQ question from the cache or translates it if not cached.

    This function checks if the translation is already cached. If it's not cached,
    it fetches the translation and stores it in the cache.

    Args:
        faq (FAQ): The FAQ object containing the question.
        lang (str): The language code (e.g., 'hi' for Hindi, 'bn' for Bengali).

    Returns:
        str: The translated FAQ question.
    """
    # Create a unique cache key for the translation based on the FAQ id and language
    cache_key = f"faq_{faq.id}_{lang}"

    # Check if the translation is already in the cache
    cached_translation = cache.get(cache_key)

    if cached_translation:
        # If the translation is cached, return it
        return cached_translation

    # If not cached, get the translation (either from the model or by translating)
    translation = getattr(faq, f"question_{lang}", None) or translate_text(
        faq.question, lang
    )

    # Cache the translation for 1 hour
    cache.set(cache_key, translation, timeout=3600)

    return translation
