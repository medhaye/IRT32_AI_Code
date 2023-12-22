from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import time
time.clock = time.time

from cleaner import clean_corpus

CORPUS_FILE = "chat.txt"

try:
    chatbot = ChatBot("Chatpot")
    trainer = ListTrainer(chatbot)
    
    # Clean and train the corpus
    cleaned_corpus = clean_corpus(CORPUS_FILE)
    trainer.train(cleaned_corpus)

    exit_conditions = (":q", "quit", "exit")
    
    while True:
        query = input("> ")
        if query.lower() in exit_conditions:
            break
        else:
            response = chatbot.get_response(query)
            print(f"🤖 {response}")

except Exception as e:
    print(f"An error occurred: {e}")



# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
# from cleaner import clean_corpus


# CORPUS_FILE = "chat.txt"

# chatbot = ChatBot("Chatpot")

# trainer = ListTrainer(chatbot)
# cleaned_corpus = clean_corpus(CORPUS_FILE)
# trainer.train(cleaned_corpus)

# exit_conditions = (":q", "quit", "exit")
# while True:
#     query = input("> ")
#     if query in exit_conditions:
#         break
#     else:
#         print(f"🪴 {chatbot.get_response(query)}")
