# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from sense_hat import SenseHat, ACTION_PRESSED

sense = SenseHat()
# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC9ea25b7cee64dc123f4f231fb05a009f'
auth_token = '9d13181de78353724603394bc472a8f3'
client = Client(account_sid, auth_token)




# Define the functions

def pushed_up(event):
  if event.action != ACTION_PRESSED:
    message = client.messages.create(
                              body='Hello there from raspi!',
                              from_='+17377779787',
                              to='+15127751780'
                          )

    print(message.sid)
    print("Message Sent")
    sense.show_letter("S")



def refresh():
    sense.clear()
    print("cleared LED")

print("This script library takes a little time as well as the time involved for Twilio API to handle the request.  It could be 30 to 60 seconds for SMS message to actually get receieved and for the success message to appear on the cli and the 'S' to be displayed on the sensehat.  Go ahead and press UP on the joystick to trigger SMS, once completed, press the joystick in the middle to refresh the led screen")
sense.stick.direction_up = pushed_up
sense.stick.direction_middle = refresh

while True:
  pass
