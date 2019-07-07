# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from sense_hat import SenseHat

sense = SenseHat()

# Define the functions

def sms():

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC9ea25b7cee64dc123f4f231fb05a009f'
auth_token = '9d13181de78353724603394bc472a8f3'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there from raspi!',
                              from_='+17377779787',
                              to='+15127751780'
                          )

print(message.sid)

# Tell the program which function to associate with which direction

sense.stick.direction_middle = sms   # Press the enter key

while True:
  pass  # This keeps the program running to receive joystick events
