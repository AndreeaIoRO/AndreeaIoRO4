import requests

class LanguageTranslator:
    def __init__(self, api_key):
        self.api_key = api_key

    def translate(self, text, source_language, target_language):
        url = f"https://translation.googleapis.com/language/translate/v2?key={self.api_key}"
        params = {
            "q": text,
            "source": source_language,
            "target": target_language
        }
        response = requests.post(url, params=params)
        data = response.json()

        if response.status_code == 200:
            translated_text = data["data"]["translations"][0]["translatedText"]
            print(f"Translation ({source_language} to {target_language}):")
            print(translated_text)
        else:
            print("Unable to perform translation.")

def main():
    api_key = "YOUR_API_KEY"
    text = "Hello, how are you?"
    source_language = "en"
    target_language = "fr"

    translator = LanguageTranslator(api_key)
    translator.translate(text, source_language, target_language)

if __name__ == "__main__":
    main()
