from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("azul")

conversation = [
    'Hola', # User
    'Hola',  # Bot
    '¿Cómo estas?',
    'bien y tu?',
    'igual'
]

trainer = ListTrainer(bot)
trainer.train(conversation)

while True:
    value = input("Tu: ")
    response = bot.get_response(value)
    print("Bot: ", response)

