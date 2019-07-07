#shutoff pixel screen with color cycle or message

from sense_hat import SenseHat
import sys

sense = SenseHat()

sense.show_message("Bye", scroll_speed=0.05, text_colour=[255,255,0], back_colour=[0,0,255])
sense.clear()
 
sys.exit()
