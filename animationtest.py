from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

r = (255, 0, 0)
o = (255, 127, 0)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 255)
i = (75, 0, 130)
v = (159, 0, 255)
e = (128, 128, 128)

colorLength = 3
colorIndex = 0
stepLength = 3
stepIndex = 0
up = True
color = e

while True:
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
  
  if colorIndex == 0:
    color = r
    up = False
    image[17] = image[18] = image[19] = image[26] = image[34] = image[42] = color
  elif colorIndex == 1:
    color = b
    up = True
    image[17] = image[19] = image[25] = image[26] = image[27] = image[33] = image[35] = image[41] = image[43] = color
  else:
    color = y
    up = False
    image[17] = image[18] = image[19] = image[25] = image[27] = image[33] = image[34] = image[35] = image[41] = color
    
  if up:
    image[stepIndex * 8 + 30] = color
    image[stepIndex * 8 + 21] = color
    image[stepIndex * 8 + 23] = color
  else:
    image[(stepLength - stepIndex - 1) * 8 + 29] = color
    image[(stepLength - stepIndex - 1) * 8 + 31] = color
    image[(stepLength - stepIndex - 1) * 8 + 22] = color
  stepIndex += 1
  
  if stepIndex == stepLength:
    stepIndex = 0
    colorIndex += 1
    if colorIndex == colorLength:
      colorIndex = 0

  sense.set_pixels(image)
  
  sleep(0.3)
