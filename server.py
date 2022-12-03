import socket
import threading
import chatbotClasses as cb

HEADER = 64 #tells the server how long the next message will be in bytes. encoded as FORMAT
PORT = 5050 #hopefully unused port
SERVER = socket.gethostbyname(socket.gethostname()) #gets localhost IP
ADDR = (SERVER, PORT) #tupple to hold host IP and port num
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT" #standard disconnect message

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) #get message length
        #if the client sent any message at all, convert the first messgae to integer length, read in that many bytes as message
        if msg_length: 
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            #if the client sent the disconnect message
            if msg == DISCONNECT_MESSAGE:
                connected = False
            #print the client message
            print(f"[{addr}] {msg}")
            #send something back
            msg = msg.removeprefix(cb.ReadInput.USERNAME + ": ")
            send(conn, cb.ReadInput.read(msg))
    #close the connection when the client disconnects
    conn.close()

def send(conn, msg):
    #encode the message
    message = msg.encode(FORMAT)
    #get the message length
    msg_length = len(message)
    #convert message length to a string encoded according to FORMAT
    send_length = str(msg_length).encode(FORMAT)
    #pad message length to be 64 bytes (append HEADER - len(send_length) spaces)
    send_length += b' ' * (HEADER - len(send_length))
    conn.send(send_length)
    conn.send(message)


def start():
    #begin listening on host IP
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    #while the server is running, accept new clients on different threads
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}\n")

def main():
    print("[STARTING] server is starting...")
    start()

if __name__=="__main__":
    main()