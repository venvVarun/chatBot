#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 22:02:37 2020
creating chatterbot
@author: rogue
"""

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
 #object for the ChatBot class and defining the name for chatbot
bot=ChatBot('Cortana')#cortana is ai name from game 
#setting the algoritham that trins chatbot
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")#train chatbot on data and language selection 

# Code to make ChatBot interactive
while(True):
    message = input('You: ')
    if(message=='Bye' or message=='bye'):
        print('{}: Nice talking. See you later'.format(bot.name))
        break
    if(message!='Bye' or message!='bye'):
        print('{}: {}'.format(bot.name, bot.get_response(message)))