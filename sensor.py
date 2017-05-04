import time # so we can use "sleep" to wait between actions
import RPi.GPIO as io # import the GPIO library we just installed but call it "io"

## name the bucket and individual access_key
## the bucket_key will send all of our messages to the same place
## the access_key tells Initial State to send the messages to you

## set GPIO mode to BCM
## this takes GPIO number instead of pin number
io.setmode(io.BCM)

## enter the number of whatever GPIO pin you're using
door_pin = 23

## use the built-in pull-up resistor
io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp

## initialize door
door=0

## this loop will execute the if statement that is true
while True:
    ## if the switch is open
    if io.input(door_pin):
        print("Desk: Going Up")
        door=0 # set door to its initial value
        time.sleep(1) # wait 1 second before the next action
        ## if the switch is closed and door does not equal 1
        if (io.input(door_pin)==False and door!=1):
            print("Desk: Seated Position")
            door=1 # set door so that this loop won't act again until the switch has been opened
