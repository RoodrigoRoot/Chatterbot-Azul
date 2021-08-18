from os import O_NDELAY
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

corbot = ChatBot("corbot")

trainer = ChatterBotCorpusTrainer(corbot)
trainer.train("chatterbot.corpus.spanish.conversations")

response = corbot.get_response("Entonces")
print(response)


