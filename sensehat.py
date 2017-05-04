from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

yellow = (255,255,0)
blue = (0, 0, 255)
green = (0,255,0)
red = (255, 0,0)
black = (0,0,0)
white = (255, 255, 255)
speed = 0.05
message = "Thinking Desk"

sense.show_message(message, speed, text_colour=yellow, back_colour=blue)

sense.clear()
sense.show_letter("4", blue)
sleep(1)
sense.show_letter("3", green)
sleep(1)
sense.show_letter("2", yellow)
sleep(1)
sense.show_letter("1", red)
sleep(1)
sense.show_letter("!", black, white)
sleep(1)
sense.clear()

