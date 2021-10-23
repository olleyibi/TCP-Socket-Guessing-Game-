
begin = "START GAME"

def start_game():
    global msg
    msg = "empty"
    begin = "START GAME"
    while True:
            print("ENTER <START GAME> TO BEGIN")
            msg = input("Client: ").upper()
            if msg == begin:
                break
            else:
                msg = "DISCONNECT"

import socket
HEADER = 64
PORT  =  6600
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def sending(message, connection):
    message=message.encode("utf-8")
    length = len(message)
    length = str(length).encode("utf-8")
    length += b" " * (64 - len(length))
    connection.send(length)
    connection.send(message)



while True:
    message = client.recv(64).decode("utf-8")
    if "GAME OVER" in message:
        print(message)
        input()
        break
    else:
        print(message)
        letter = input("CLIENT: ")
        sending(letter,client)

