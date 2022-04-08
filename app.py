#imports

from logging import WARNING, FileHandler,WARNING
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from train import *
from filterquestions import *
from getData import *


app = Flask(__name__)

File_Handler=FileHandler('errorlog.txt')
File_Handler.setLevel(WARNING)
#create chatbot
print("Started...")
chatbot = ChatBot("Sisly Chatbot", storage_adapter="chatterbot.storage.SQLStorageAdapter", read_only=True,logic_adapter=["chatterbot.logic.BestMatch",'chatterbot.logic.MathematicalEvaluation','chatterbot.logic.TimeLogicAdapter'],preprocessors=['chatterbot.preprocessors.clean_whitespace'])
trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.train("chatterbot.corpus.english") #train the chatter bot for english
'''def datat(d):
    a=get_Attendence(d)
    print(a+"yuyu")
datat(39)'''
trainer1 = ListTrainer(chatbot)
trainer1.train(data)
trainer1.train(data1)
trainer1.train(attendenceConvo)

#define app routes
@app.route("/")
def index():
    return render_template("index1.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')

    if userText[:8] == "rollno::":
        RollNo=userText[8:]
        print(RollNo)
        attendence=get_Attendence(RollNo)
        return str(attendence)
    elif userText not in filter:
        return str("Sorry not in database!")

    bot_response=chatbot.get_response(userText)
    return str(bot_response)

if __name__ == "__main__":
    app.run()