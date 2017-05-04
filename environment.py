#!/usr/bin/env python3

import os
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

def get_cpu_temp():
    res = os.popen("vcgencmd measure_temp").readline()
    t = float(res.replace("temp=","").replace("'C\n",""))
    return(t)


def get_smooth(x):
    if not hasattr(get_smooth,"t"):
        get_smooth.t = [x,x,x]
    get_smooth.t[2] = get_smooth.t[1]
    get_smooth.t[1] = get_smooth.t[0]
    get_smooth.t[0] = x
    xs = (get_smooth.t[0]+get_smooth.t[1]+get_smooth.t[2])/3
    return(xs)


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
    #t = sense.get_temperature();
    th = sense.get_temperature_from_humidity()
    tp = sense.get_temperature_from_pressure()
    t_cpu = get_cpu_temp()
    thp = (th+tp)/2
    t = thp - ((t_cpu-thp)/1.5)
    t = get_smooth(t)
    t = round(t,1)
    reportstate("temperature",t);

    p = sense.get_pressure();
    p = round(p,1)
    reportstate("pressure",p);

    h = sense.get_humidity();
    h = round(h,1);
    reportstate("humidity",h);

    print("Temp = {0}, Pressure = {1}, Humidity = {2}".format(t, p, h))

    time.sleep(5)

