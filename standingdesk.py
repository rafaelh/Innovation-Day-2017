import time
import sys
from azure.servicebus import ServiceBusService
import RPi.GPIO as io

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

while True:
    if io.input(DESK_PIN):
        # The switch is open
        print("Desk: Standing Position. Sending to Azure... ", end='')
        try:
            SBS.send_event('stand-and-deliver',
                           '{ "DeviceId": "StandingDesk1", "State": "Standing" }')
            print("done.")
        except:
            print("sending failed.")

    if io.input(DESK_PIN)==False:
        # The switch is closed
        print("Desk: Seated Position. Sending to Azure... ", end='')
        try:
            SBS.send_event('stand-and-deliver', '{ "DeviceId": "StandingDesk1", "State": "Seated" }')
            print("done.")
        except:
            print("sending failed.")

    time.sleep(10)
