"""
    Chatbot para reservar la entrada para una pelicula.
"""
from chatterbot import ChatBot
from chatterbot import trainers
from chatterbot.trainers import ListTrainer

movie_chat = ChatBot("MovieChat")

trainer = ListTrainer(movie_chat)

QUESTION = "Hola, ¿Quieres ver la cartelera de películas?"
MOVIES = "1.-Black Widow\n2.-Escuadrón Suicida 2\n3.- un Jefe en pañales"

conversations = ["Hola", 
                 QUESTION,
                 "Buenas tardes",
                 QUESTION,
                 "Buenas",
                 QUESTION,
                 "Buenas noches",
                 QUESTION,
                 "Buenos días",
                 QUESTION,
                 "Buenos dias",
                 QUESTION,
                 "Buenas, Disculpe",
                 QUESTION,
                 "Buenas buenas",
                 QUESTION,
                 "Holis",
                 QUESTION,
                 "¿Qué tal?",
                 QUESTION,
                 "Que tal?",
                 QUESTION,
                 "Si",
                 MOVIES,
                 "si, por favor",
                 MOVIES,
                 "Si, gracias",
                 MOVIES,
                 "claro",
                 MOVIES,
                 ]
trainer.train(conversations)

dict_movies = {1:"Black Widow", 2:"Escuadrón Suicida 2", 3:"Un Jefe en Pañales"}

def movie_reservation(connection, option):
    movie = dict_movies.get(option, "")
    # si movie = "Black Widow -> Significa que la condición se cumple"
    # si movie = "" -> Significa que la condición no se cumple
    if movie:
        connection.send(str.encode("¿Cuál es tu nombre?"))
        name = connection.recv(1024)
        name = name.decode("utf-8")
        with open("reservations.txt", "a+") as file:
            file.write(f"Reservación\nNombre: {name} - Pelicula: {movie}\n")
        return "Su reservación ha sido registrada. Muchas gracias por usar MovieChat"

    else:
        return f"Por favor revise de nuevo la cartelera.\n{MOVIES}"



