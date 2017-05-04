#!/usr/bin/env python3

import time
from azure.servicebus import ServiceBusService
import RPi.GPIO as io

LAST_STATE = ''
TIME_IN_STATE = time.time()
DESK_PIN = 23
KEY_NAME = "RootManageSharedAccessKey"
KEY_VALUE = "pjxZvmffk+hhDTXST7TzvShuZ+jxgRiKLc1T4yLGOGw="
SBS = ServiceBusService("stand-and-deliver",
                        shared_access_key_name=KEY_NAME,
                        shared_access_key_value=KEY_VALUE)

# Set GPIO mode to BCM, using the GPIO number (in this case, 23)
io.setmode(io.BCM)

# Activate input with the built-in PullUp resistor
io.setup(DESK_PIN, io.IN, pull_up_down=io.PUD_UP)

def reportstate(state):
    " Prints state to the console and sends to Azure "
    print("Desk: {} position. Sending to Azure...".format(state), end='')
    event = '{ "DeviceId": "StandingDesk1", "State": "%s" }' % state
    try:
        SBS.send_event('stand-and-deliver', event)
        print("done.")
    except:
        print("sending failed.")

while True:
    if io.input(DESK_PIN):
        STATE = 'Standing'
        reportstate(STATE)

    if not io.input(DESK_PIN):
        STATE = 'Seated'
        reportstate(STATE)

    if STATE != LAST_STATE:
        CURRENT_TIME = time.time()
        print("State Changed. Time in last state: ", CURRENT_TIME - TIME_IN_STATE)

    LAST_STATE = STATE
    time.sleep(5)
