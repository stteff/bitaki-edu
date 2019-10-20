from microbit import *
from time import sleep

while True:
    print((accelerometer.get_x(), accelerometer.get_y()))
    sleep(0.025)