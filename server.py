# server
import random
import socket
import threading

def sending(message, connection):
    message=message.encode("utf-8")
    length = len(message)
    length = str(length).encode("utf-8")
    length += b" " * (64 - len(length))
    connection.send(length)
    connection.send(message)


def receive(connection):
    rec = connection.recv(64).decode("utf-8")
    if rec:
        rec=int(rec)
        mes = connnection.recv(rec).decode("utf-8")
    return mes



HEADER = 64
PORT  =  6600
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected")
    
    while True:
        import random
        word_list = ['APPLE', 'HELLO', 'LAMINATE', 'SORCERER', 'WILLOW']
        word=random.choice(word_list)
        line = len(word)*"_ "
        reply = ""
        count = 0
        while count<len(word)+1:
            conn.send(f"SERVER: {line}".encode(FORMAT))
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                letter = conn.recv(msg_length).decode(FORMAT)
                if letter.upper() == word[count]:
                    count+=1
                    line = word[0:count]+(len(word)-count)*" _"
                    if count == len(word):
                        conn.send((f"The word is {word}, GAME OVER").encode(FORMAT))

                        conn.close()
    

    
    
        
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting....")
start()
