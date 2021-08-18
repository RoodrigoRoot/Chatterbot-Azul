import socket
from _thread import start_new_thread
from bot import movie_reservation, movie_chat

serversocket = socket.socket()

HOST = "192.168.100.2"
PORT = 1233
is_on = True

try:

    serversocket.bind((HOST, PORT))
    serversocket.listen(5)

    print("Running..........")
except Exception as e:
    print(e)
    is_on = False
    serversocket.close()


def client_chatbot_thread(connection):
    connection.send(str.encode("Bienvendio a MovieChat. Reservación de  Peliculas"))

    while True:
        data = connection.recv(1024)#Bytes
        data = data.decode("utf-8")
        reply = ""
        try:
            option = int(data)
            reply = movie_reservation(connection, option)
            connection.sendall(str.encode(reply))
            break
        except Exception as e:
            reply = movie_chat.get_response(data)
            connection.sendall(str.encode(reply.text))

    connection.close()


while is_on:
    client, address = serversocket.accept()
    start_new_thread(client_chatbot_thread, (client, ))


serversocket.close()