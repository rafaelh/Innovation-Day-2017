from sense_hat import SenseHat
import time
import math
import misc


sense = SenseHat()
sleepy_time = 2


def flashArrow(arrowDirection):
    x = 0
    misc.play_alarm()
    if arrowDirection == 1:
      while x < 4:
        misc.up_arrow()
        time.sleep(0.6)
        set_region(5,1,7,6,misc.O,0)
        time.sleep(0.6)
        x = x + 1
    if arrowDirection == 0:
      while x < 4:
        misc.down_arrow()
        time.sleep(0.6)
        set_region(5,1,7,6,misc.O,0)
        time.sleep(0.6)
        x = x + 1


def set_region(startx, starty, endx, endy, color, addNumber):
  for y in range(starty, endy+1):
    for x in range(startx, endx+1):
      sense.set_pixel(x,y,color)
      
  if (addNumber > 0):
    for x in range (0,addNumber):
      sense.set_pixel(startx+x,starty-1,misc.X)
      
def timer(startMins, state):
  sense.clear()  
  while startMins > 0:
    segments = startMins / 10 # 10
    totalRows = segments / 4 # 2.50
    printRows = math.floor(totalRows)
    remainder = totalRows - printRows
    addNumber = remainder / 0.25
    if state == 1:
      misc.up_arrow()
    if state == 0:
      misc.down_arrow()
      
    set_region(0,7-(int(printRows)),3,6,misc.X,int(addNumber))
    time.sleep(1)
    startMins = startMins - 10
    sense.clear()
    
  if state == 1:
    alternateState = 0
  if state == 0:
    alternateState = 1

  flashArrow(alternateState)


    

    
  
