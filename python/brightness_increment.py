from microbit import *

bright = 0
pin0.write_analog(bright)
while True:

    if button_a.is_pressed():
        bright = bright + 100
        pin0.write_analog(bright)
            
    if button_b.is_pressed():
        bright = bright - 100
        pin0.write_analog(bright)


        
