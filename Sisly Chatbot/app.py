#imports
from logging import WARNING, FileHandler,WARNING
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from train import *

app = Flask(__name__)

File_Handler=FileHandler('errorlog.txt')
File_Handler.setLevel(WARNING)
#create chatbot
chatbot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english") #train the chatter bot for english

trainer1 = ListTrainer(chatbot)
trainer1.train(data)
trainer1.train(data1)

#define app routes
@app.route("/")
def index():
    return render_template("index1.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

if __name__ == "__main__":
    app.run()