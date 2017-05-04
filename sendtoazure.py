import time
import sys
from azure.servicebus import ServiceBusService

key_name="My Sender"
key_value="Insert Key"

sbs = ServiceBusService("robotdeskeventhub-ns",
                       shared_access_key_name=key_name,
                       shared_access_key_value=key_value)

while(True):
    print('Sending...')
    sbs.send_event('nameofeventhub', '{ "DeviceId": "StandingDesk",
                   "State": "Standing or Seated" }')
    print('Sent...')
    time.sleep(10)

