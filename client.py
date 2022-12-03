import socket
import chatbotClasses as cb

#see server.py for constant meanings
HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
MAX_MESSAGES = 15

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg, count):
    #encode the message
    message = msg.encode(FORMAT)
    #get the message length
    msg_length = len(message)
    #convert message length to a string encoded according to FORMAT
    send_length = str(msg_length).encode(FORMAT)
    #pad message length to be 64 bytes (append HEADER - len(send_length) spaces)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

    msg_length = client.recv(HEADER).decode(FORMAT) #get message length
    #if the server sent any message at all, convert the first messagee to integer length, read in that many bytes as message
    if msg_length: 
        msg_length = int(msg_length)
        msg = client.recv(msg_length).decode(FORMAT)

        print(msg)
        if count < MAX_MESSAGES:
            msg = msg.removeprefix(cb.ReadInput.USERNAME + ": ")
            send(cb.ReadInput.read(msg), count+1)

def main():
    send(f"{cb.ReadInput.USERNAME}: sup", 1)

    send(DISCONNECT_MESSAGE, MAX_MESSAGES+1)

if __name__=="__main__":
    main()
