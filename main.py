from translator import translate_text

if __name__ == "__main__":
    text = input("Enter text to translate: ")
    lang = input("Enter target language code (e.g., 'hi' for Hindi, 'es' for Spanish): ")
    result = translate_text(text, dest_language=lang)
    print("Translated:", result)
