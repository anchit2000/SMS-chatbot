from ipaddress import IPv4Address  # for your IP address
from pyairmore.request import AirmoreSession  # to create an AirmoreSession
from pyairmore.services.messaging import MessagingService  # to send messages

import time
import random
import schedule
import subprocess
import utils

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

ip = IPv4Address("192.168.0.108")  # let's create an IP address object
# now create a session
session = AirmoreSession(ip)
# if your port is not 2333
# session = AirmoreSession(ip, 2334)  # assuming it is 2334

session.is_server_running  # True if Airmore is running

was_accepted = session.request_authorization()

print(was_accepted)  # True if accepted

service = MessagingService(session)
#service.send_message("8264096066", "Hello")

def send_message(number,response):
	service.send_message(number, response)
#send_message()

'''
schedule.every().day.at("14:06").do(send_message)
print("Message was sent")

while True:
	schedule.run_pending()
	time.sleep(1)
'''

bot = ChatBot("My Bot")
convo = [
         'hello',
         'hi there!',
         'what is your name?',
         'My name is bot, I am created by Anchit',
         'how are you?',
         'I am good, thank you. How are you?',
         'i am also good',
         'Great!',
         'bye',
         'have a great day'
]
trainer = ListTrainer(bot)
trainer.train(convo)
test = ""
while True:
	messages = service.fetch_message_history()
	if messages[0].was_read == False and test!=messages[0].content:
		request = messages[0].content
		response = bot.get_response(request)
		send_message(messages[0].phone,response)
		test = request
