import socket

clientsocket = socket.socket()
HOST = "127.0.0.1"
PORT = 1233

is_connect = True

try:
    clientsocket.connect((HOST, PORT))
    response = clientsocket.recv(1024)
    print(response.decode("utf-8"))

except Exception as e:
    print("Problemas de conexión, por favor intente más tarde.")
    is_connect = False


while is_connect:
    msg = input("Tu: ")
    clientsocket.send(str.encode(msg))
    response = clientsocket.recv(1024)
    response = response.decode("utf-8")
    print(f"Bot: {response}")