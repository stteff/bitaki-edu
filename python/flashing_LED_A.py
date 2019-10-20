from microbit import *
from time import sleep

while True:
    if button_a.is_pressed():
        for i in range(3):
            pin0.write_digital(1)
            sleep(0.5)
            pin0.write_digital(0)
            sleep(0.5)
            


        
