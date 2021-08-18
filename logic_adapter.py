from chatterbot import ChatBot
from chatterbot.logic import logic_adapter

logic_chatbot = ChatBot("logic_chatbot",
                        logic_adapters = [
                            'chatterbot.logic.MathematicalEvaluation',
                            'chatterbot.logic.TimeLogicAdapter',
                        ]
                        )


while True:
    value = input("Tu: ")
    response =  logic_chatbot.get_response(value)
    print(response)