from googletrans import Translator

# These should match your app's supported codes
VALID_LANG_CODES = ['hi', 'fr', 'es', 'de', 'ja', 'zh-cn', 'ru', 'ar', 'ko', 'en']

def translate_text(text, source_language='auto', dest_language='en'):
    try:
        if source_language != 'auto' and source_language not in VALID_LANG_CODES:
            raise ValueError(f"Invalid source language: {source_language}")
        if dest_language not in VALID_LANG_CODES:
            raise ValueError(f"Invalid destination language: {dest_language}")

        translator = Translator()
        result = translator.translate(text, src=source_language, dest=dest_language)

        if result is None:
            return "Error: Translation result is None."

        return result.text

    except ValueError as ve:
        return f"Error: {ve}"

    except Exception as e:
        return f"An error occurred during translation: {str(e)}"

   
