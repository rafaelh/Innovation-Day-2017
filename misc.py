from sense_hat import SenseHat
import time
from pygame import mixer
import pygame

sense = SenseHat()

B = [0, 0, 255]  # Blue
X = [255, 0, 0]  # Red
O = [0, 0, 0]    # Black

def up_arrow():
    """ Display an up arrow on the sense hat """
    sense.set_pixel(6, 1, B)
    sense.set_pixel(5, 2, B)
    sense.set_pixel(7, 2, B)
    sense.set_pixel(6, 2, B)
    sense.set_pixel(6, 3, B)
    sense.set_pixel(6, 4, B)
    sense.set_pixel(6, 5, B)
    sense.set_pixel(6, 6, B)

def down_arrow():
    """ Display a down arrow on the sense hat """
    sense.set_pixel(6, 1, B)
    sense.set_pixel(5, 5, B)
    sense.set_pixel(7, 5, B)
    sense.set_pixel(6, 2, B)
    sense.set_pixel(6, 3, B)
    sense.set_pixel(6, 4, B)
    sense.set_pixel(6, 5, B)
    sense.set_pixel(6, 6, B)

def play_alarm():
    """ Play the specified mp3 file """
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("alarm2.mp3")
    pygame.mixer.music.play()
    time.sleep(1.1)
    pygame.mixer.music.stop()
    pygame.mixer.quit()

numbers = [
    [
        O, O, O, O, O, O, O, O,
        O, X, X, O, O, O, O, O,
        X, O, O, X, O, O, O, O,
        X, O, O, X, O, O, O, O,
        X, O, O, X, O, O, O, O,
        X, O, O, X, O, O, O, O,
        O, X, X, O, O, O, O, O,
        O, O, O, O, O, O, O, O
    ], # zero
    [
        O, O, O, O, O, O, O, O,
        O, O, X, O, O, O, O, O,
        O, O, X, O, O, O, O, O,
        O, O, X, O, O, O, O, O,
        O, O, X, O, O, O, O, O,
        O, O, X, O, O, O, O, O,
        O, O, X, O, O, O, O, O,
        O, O, O, O, O, O, O, O
    ], # one
    [
        O, O, O, O, O, O, O, O,
        X, X, X, X, O, O, O, O,
        O, O, O, X, O, O, O, O,
        O, O, O, X, O, O, O, O,
        X, X, X, X, O, O, O, O,
        X, O, O, O, O, O, O, O,
        X, X, X, X, O, O, O, O,
        O, O, O, O, O, O, O, O
    ], # two
    [
        O, O, O, O, O, O, O, O,
        X, X, X, X, O, O, O, O,
        O, O, O, X, O, O, O, O,
        O, O, O, X, O, O, O, O,
        X, X, X, X, O, O, O, O,
        O, O, O, X, O, O, O, O,
        X, X, X, X, O, O, O, O,
        O, O, O, O, O, O, O, O
    ], # three
    [
        O, O, O, O, O, O, O, O,
        X, O, O, X, O, O, O, O,
        X, O, O, X, O, O, O, O,
        X, O, O, X, O, O, O, O,
        X, X, X, X, O, O, O, O,
        O, O, O, X, O, O, O, O,
        O, O, O, X, O, O, O, O,
        O, O, O, O, O, O, O, O
    ], # four
    [
        O, O, O, O, O, O, O, O,
        X, X, X, X, O, O, O, O,
        X, O, O, O, O, O, O, O,
        X, O, O, O, O, O, O, O,
        X, X, X, X, O, O, O, O,
        O, O, O, X, O, O, O, O,
        X, X, X, O, O, O, O, O,
        O, O, O, O, O, O, O, O
    ], # five
    [
        O, O, O, O, O, O, O, O,
        X, X, X, X, O, O, O, O,
        X, O, O, O, O, O, O, O,
        X, O, O, O, O, O, O, O,
        X, X, X, X, O, O, O, O,
        X, O, O, X, O, O, O, O,
        O, X, X, O, O, O, O, O,
        O, O, O, O, O, O, O, O
    ], # six
    [
        O, O, O, O, O, O, O, O,
        O, X, X, X, O, O, O, O,
        O, O, O, X, O, O, O, O,
        O, O, O, X, O, O, O, O,
        O, O, O, X, O, O, O, O,
        O, O, O, X, O, O, O, O,
        O, O, O, X, O, O, O, O,
        O, O, O, O, O, O, O, O
    ], # seven
    [
        O, O, O, O, O, O, O, O,
        O, X, X, O, O, O, O, O,
        X, O, O, X, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, X, X, O, O, O, O, O,
        X, O, O, X, O, O, O, O,
        O, X, X, O, O, O, O, O,
        O, O, O, O, O, O, O, O
    ], # eight
    [
        O, O, O, O, O, O, O, O,
        X, X, X, X, O, O, O, O,
        X, O, O, X, O, O, O, O,
        X, O, O, X, O, O, O, O,
        X, X, X, X, O, O, O, O,
        O, O, O, X, O, O, O, O,
        X, X, X, O, O, O, O, O,
        O, O, O, O, O, O, O, O
    ] # nine
]
