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
# Colors
r = (255, 0, 0)
o = (255, 127, 0)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 255)
i = (75, 0, 130)
v = (159, 0, 255)
e = (0, 0, 0)

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

def updatedisplay(pageIndex, stepIndex, delta):
    " Update display "

    stepLength = 3 # Assuming three frames of animation
    color = e
    image = [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e
    ]

    if pageIndex == 0:
        color = r
        image[17] = image[18] = image[19] = image[26] = image[34] = image[42] = color
    elif pageIndex == 1:
        color = b
        image[17] = image[19] = image[25] = image[26] = image[27] = image[33] = image[35] = image[41] = image[43] = color
    else:
        color = y
        image[17] = image[18] = image[19] = image[25] = image[27] = image[33] = image[34] = image[35] = image[41] = color

    if delta > 0:
        image[stepIndex * 8 + 30] = color
        image[stepIndex * 8 + 21] = color
        image[stepIndex * 8 + 23] = color
    elif delta < 0:
        image[(stepLength - stepIndex - 1) * 8 + 29] = color
        image[(stepLength - stepIndex - 1) * 8 + 31] = color
        image[(stepLength - stepIndex - 1) * 8 + 22] = color
    else:
        image[37] = image[38] = image[39] = color

    sense.set_pixels(image)

oldt = 0
oldh = 0
oldp = 0
while True:
    th = sense.get_temperature_from_humidity()
    tp = sense.get_temperature_from_pressure()
    t_cpu = get_cpu_temp()
    thp = (th+tp)/2
    t = thp - ((t_cpu-thp)/1.5)
    t = get_smooth(t)
    t = round(t,1)
    reportstate("Temperature",t)

    diff = 0
    if oldt != 0:
        diff = oldt - t
    oldt = t
    updatedisplay(0,0,diff)
    time.sleep(0.4)
    updatedisplay(0,1,diff)
    time.sleep(0.4)
    updatedisplay(0,2,diff)
    time.sleep(0.4)

    p = sense.get_pressure()
    p = round(p,1)
    reportstate("Pressure",p)

    diff = 0
    if oldp != 0:
        diff = oldp - p
    oldp = p
    updatedisplay(2,0,diff)
    time.sleep(0.4)
    updatedisplay(2,1,diff)
    time.sleep(0.4)
    updatedisplay(2,2,diff)
    time.sleep(0.4)

    h = sense.get_humidity()
    h = round(h,1);
    reportstate("Humidity",h)

    diff = 0
    if oldh != 0:
        diff = oldh - h
    oldh = h
    updatedisplay(1,0,diff)
    time.sleep(0.4)
    updatedisplay(1,1,diff)
    time.sleep(0.4)
    updatedisplay(1,2,diff)
    time.sleep(0.4)

    print("Temp = {0}, Pressure = {1}, Humidity = {2}".format(t, p, h))

