# This file has been written to your home directory for convenience. It is
# saved as "/home/pi/plumb_line-2018-07-07-19-45-06.py"

from time import sleep
from sense_hat import SenseHat
from PIL import Image, ImageDraw

hat = SenseHat()

hat.clear()
origin = (7, 7)
while True:
    a = hat.get_accelerometer_raw()
    # Use the old trick of drawing something too big then down-sizing to get an
    # anti-aliased line
    img = Image.new('RGB', (15, 15))
    draw = ImageDraw.Draw(img)
    dest = (origin[0] + a['x'] * 7.0, origin[1] + a['y'] * 7.0)
    draw.line([origin, dest], fill=(255, 255, 255), width=3)
    img = img.resize((8, 8), Image.BILINEAR)
    hat.set_pixels(list(img.getdata()))
    sleep(0.04)
