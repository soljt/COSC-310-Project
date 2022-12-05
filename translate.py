from googletrans import Translator
def translateInput(userInput):
    translator = Translator()
    translation = translator.translate(userInput, dest='en')
    # print(translation.text)
    return translation.text

def detectEnglish(userInput):
    translator = Translator()
    lang = translator.detect(userInput)
    if lang.lang=='en':
        return True
    else:
        return False

def main():
    userInput = "quel age as tu"

    translator = Translator()
    lang = translator.detect(userInput)
    print(lang.lang)

    translation = translator.translate(userInput, dest='en')
    print(translation.text)

if __name__ == "__main__":
    main()
