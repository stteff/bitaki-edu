from microbit import *
import music

while True:

    if button_a.is_pressed():
        pin0.write_digital(1)
            
    if button_b.is_pressed():
        pin0.write_digital(0)

    if button_a.is_pressed() and button_b.is_pressed():
        music.play(music.ENTERTAINER)
        
