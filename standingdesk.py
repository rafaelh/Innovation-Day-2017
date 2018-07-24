#!/usr/bin/env python3

import time
import datetime
from azure.servicebus import ServiceBusService
import RPi.GPIO as io

LAST_STATE = ''
TIME_IN_STATE = time.time()
DESK_PIN = 23
KEY_NAME = "e.g. RootManageSharedAccessKey"
KEY_VALUE = "e. g. pjxZvmffk+h... etc"
SBS = ServiceBusService("InsertYourNamespace",
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

print("Polling every 5 seconds...")
while True:
    if io.input(DESK_PIN):
        STATE = 'Standing'
        reportstate(STATE)

    if not io.input(DESK_PIN):
        STATE = 'Seated'
        reportstate(STATE)

    if STATE != LAST_STATE:
        CURRENT_TIME = time.time()
        ELAPSED_TIME = str(datetime.timedelta(seconds=int(CURRENT_TIME - TIME_IN_STATE)))
        print("State Changed. Time in last state:", ELAPSED_TIME)

    LAST_STATE = STATE
    time.sleep(5)
