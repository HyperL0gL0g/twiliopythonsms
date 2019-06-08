# importing twilio 
from twilio.rest import Client 

# Your Account Sid and Auth Token from twilio.com / console 
account_sid = 'PASTE YOUR OWN SID BY REGISTERING AT TWILIO'
auth_token = 'PASTE YOUR OWN TOKEN BY REGISTERING AT TWILIO'

client = Client(account_sid, auth_token) 

message = client.messages.create( 
							from_="REPLACE WITH TWILIO TRIAL/PAID NUMBER", 
							body =" (SAMPLE MESSAGE) EDEN HAZARD JOINS REAL MADRID!!", 
							to ="THE NUMBER WHERE YOU WANT TO SEND SMS TO"
						) 

print(message.sid) 
