from sense_hat import SenseHat
import time

sense = SenseHat()

p = (204, 0, 204) # pink
g = (0, 102, 102) # green
w = (200, 200, 200) # white
y = (204, 204, 0) # yellah
e = (0, 0, 0) # empty

pet1 = [
e, e, e, e, e, e, e, e,
p, e, e, e, e, e, e, e,
e, p, e, e, p, e, p, e,
e, p, g, g, p, y, y, e,
e, g, g, g, y, w, y, g,
e, g, g, g, g, y, y, e,
e, g, g, g, e, g, e, e,
e, e, e, e, e, e, e, e,
]

pet2 = [
e, e, e, e, e, e, e, e,
p, e, e, e, e, e, e, e,
e, p, e, e, p, e, p, e,
e, p, g, g, p, y, y, e,
e, g, g, g, y, w, y, g,
e, g, g, g, g, y, y, e,
e, g, e, g, e, g, e, e, 
e, e, e, e, e, e, e, e, 
]


def walking():

	for i in range(10):
		sense.set_pixels(pet1)
		time.sleep(0.5)
		sense.set_pixels(pet2)
		time.sleep(0.5)

sense.clear()

x, y, z = sense.get_accelerometer_raw().values()

while x < 2 and y < 2 and z < 2:
	x, y, z = sense.get_accelerometer_raw().values()
	walking()



