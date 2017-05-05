from sense_hat import SenseHat
import time
import misc

sense = SenseHat()


sleepy_time = 2

def set_region(startx, starty, endx, endy, color):
  for y in range(starty, endy+1):
    for x in range(startx, endx+1):
      sense.set_pixel(x,y,color)

X = misc.X
O = misc.O

numbers = misc.numbers

def flashArrow(arrowDirection):
    x = 0
    misc.play_alarm()
    if arrowDirection == 1:
      while x < 4:
        misc.up_arrow()
        time.sleep(0.6)
        set_region(5,1,7,6,O)
        time.sleep(0.6)
        x = x + 1
    if arrowDirection == 0:
      while x < 4:
        misc.down_arrow()
        time.sleep(0.6)
        set_region(5,1,7,6,O)
        time.sleep(0.6)
        x = x + 1
      
# demo to set up or down in hours, 
# will wait 5 seconds then tick 
def demoChangeStart(hours, state):
  sense.clear()
  sense.set_pixels(numbers[hours])
  while hours > 0:
    if state == 1:
      misc.up_arrow()
    if state == 0:
      misc.down_arrow()
    time.sleep(2)
    hours = hours - 1
    set_region(5,1,5,7,O)
    sense.set_pixels(numbers[hours])
  sense.set_pixels(numbers[0])
  
  if state == 0:
    newState = 1
  else:
    newState = 0
    
  flashArrow(newState)
  
