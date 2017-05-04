import time
import sys
from azure.servicebus import ServiceBusService
import RPi.GPIO as io

key_name="RootManageSharedAccessKey"
key_value="pjxZvmffk+hhDTXST7TzvShuZ+jxgRiKLc1T4yLGOGw="

SBS = ServiceBusService("stand-and-deliver",
                        shared_access_key_name=key_name,
                        shared_access_key_value=key_value)

## Set GPIO mode to BCM, busing the GPIO number (in this case, 23)
io.setmode(io.BCM)
desk_pin = 23

## Use the built-in PullUp resistor & initialize the desk switch
io.setup(desk_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp
DESK = 1

while True:
    if io.input(desk_pin):
        # The switch is open
        print("Desk: Standing Position. Sending to Azure...",)
        SBS.send_event('stand-and-deliver', '{ "DeviceId": "StandingDesk1", "State": "Standing" }')
        print("done.")
#        DESK = 0 # set door to its initial value
        time.sleep(10) # wait 10 seconds before the next action
        ## if the switch is closed and door does not equal 1
        if (io.input(desk_pin)==False):
            print("Desk: Seated Position. Sending to Azure...")
            SBS.send_event('stand-and-deliver', '{ "DeviceId": "StandingDesk1", "State": "Seated" }')
            print("done.")
#            DESK = 1
            # set door so that this loop won't act again until the switch has been opened
