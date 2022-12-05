from google.cloud import translate
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/soljt/Documents/COSC 310/IndividualProject/chatbot/key.json"
def translate_text(text="Quel age as tu", project_id="cosc310-370602"):
    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"

    response = client.translate_text(
    request={
        "parent": parent,
        "contents": [text],
        "mime_type": "text/plain",
        "target_language_code": "en-US",
    }
    )

    for translation in response.translations:
        return("{}".format(translation.translated_text))

def detect_language_en(text):
    client = translate.TranslationServiceClient()
    response = client.detect_language(parent="projects/cosc310-370602", content=text)

    for languages in response.languages:
        confidence = languages.confidence
        language_code = languages.language_code
        if language_code == "en":
            return True
        else:
            return False
        # print(
        #     f"Confidence: {confidence:6.1%}",
        #     f"Language: {language_code}",
        #     text,
        #     sep=" | ",
        # )


# sentences = (
#     "Hola Mundo!",
#     "Hallo Welt!",
#     "Bonjour le Monde !",
# )
# for sentence in sentences:
#     detect_language(sentence)

# detect_language("bonjour, comment t'apelles tu")

def main():
    print(translate_text("Comment ca va"))

if __name__ == "__main__":
    main()