#!/usr/bin/env python3

from sense_hat import SenseHat
import time
from azure.servicebus import ServiceBusService
import RPi.GPIO as io

sense = SenseHat()

KEY_NAME = "RootManageSharedAccessKey"
KEY_VALUE = "pjxZvmffk+hhDTXST7TzvShuZ+jxgRiKLc1T4yLGOGw="
SBS = ServiceBusService("stand-and-deliver",
			shared_access_key_name=KEY_NAME,
			shared_access_key_value=KEY_VALUE)


def reportstate(environment, state):
	" Prints state to the console and sends to Azure "
	print("Sending to Azure...".format(state))
	event = '{ "DeviceId": "StandingDesk1", "{}": "{}" }'.format(environment,state)
	try:
		SBS.send_event('environment', event)
		print("done.")
	except:
		print("sending failed.")



while True:
	t = sense.get_temperature()
	t = round(t, 1)
	print("temperature : {0}".format(t))

	reportstate("desk1", t)

	time.sleep(5)


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

