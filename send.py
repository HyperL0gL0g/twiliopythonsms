# importing twilio 
from twilio.rest import Client 

# Your Account Sid and Auth Token from twilio.com / console 
account_sid = 'AC057dcec475148e15b942f27275acab48'
auth_token = '20b8dca75f53aa2f17471f44d8dcf2de'

client = Client(account_sid, auth_token) 

''' Change the value of 'from' with the number 
received from Twilio and the value of 'to' 
with the number in which you want to send message.'''
message = client.messages.create( 
							from_="+12105298640", 
							body ="EDEN HAZARD JOINS REAL MADRID!!", 
							to ="+917003896831"
						) 

print(message.sid) 
