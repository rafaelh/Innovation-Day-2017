import time
import sys
from azure.servicebus import ServiceBusService

key_name="RootManageSharedAccessKey"
key_value="pjxZvmffk+hhDTXST7TzvShuZ+jxgRiKLc1T4yLGOGw="

sbs = ServiceBusService("stand-and-deliver",
                       shared_access_key_name=key_name,
                       shared_access_key_value=key_value)

while(True):
    print('Sending...')
    sbs.send_event('stand-and-deliver', '{ "DeviceId": "StandingDesk1", "State": "Standing or Seated" }')
    print('Sent...')
    time.sleep(10)

