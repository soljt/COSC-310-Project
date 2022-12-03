import chatbotClasses
def main():
    while True:
        userInput = input("You: ")
        op = chatbotClasses.ReadInput.read(userInput)
        print(op)
        
if __name__ == "__main__":
    main()