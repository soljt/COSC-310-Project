import chatbotClasses
import login
from PIL import Image
def main():
    result = False
    while not result:
        print("Please log in to continue to chat site.")
        username = input("Username: ")
        password = input("Password: ")
        result = login.validate(username,password)
        if result:
            print("Login succesful! You are now chatting with " + chatbotClasses.ReadInput.USERNAME)
        else:
            print("Login failed. Press enter to try again.")
            input()
    while True:
        userInput = input(username + ": ")
        op, associatedImg = chatbotClasses.ReadInput.read(userInput)
        print(op)
        if associatedImg != "":
            img = Image.open(associatedImg)
            img.show()
if __name__ == "__main__":
    main()