#!/usr/bin/env python3

import time
from azure.servicebus import ServiceBusService
from sense_hat import SenseHat
import RPi.GPIO as io

sense = SenseHat()

KEY_NAME = "RootManageSharedAccessKey"
KEY_VALUE = "pjxZvmffk+hhDTXST7TzvShuZ+jxgRiKLc1T4yLGOGw="
SBS = ServiceBusService("stand-and-deliver",
                        shared_access_key_name=KEY_NAME,
                        shared_access_key_value=KEY_VALUE)
                                                

def reportstate(environment, state):
    " Prints state to the console and sends to Azure "
    #print("Sending to Azure...")
    event = '{ "DeviceId": "StandingDesk2", "%s": "%s" }' % (environment,state)
    #print(event)

    try:
        SBS.send_event('stand-and-deliver', event)
        print("done.")
    except:
        print("sending failed.")
        
        
        
while True:
    t = sense.get_temperature();
    t = round(t,1)
    reportstate("temperature",t-9);

    p = sense.get_pressure();
    p = round(p,1)
    reportstate("pressure",p);

    h = sense.get_humidity();
    h = round(h,1);
    reportstate("humidity",h);

    time.sleep(5)

