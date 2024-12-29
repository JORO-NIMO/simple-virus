import rotatescreen
import time
screen = rotatescreen.get_primary_display()
#you can change the range to any number u like for the screen to rotate as many times as u want
#the screen can only be roates by 90 each time and that is why you use i*90
for i in range (10):
    time.sleep(1)
    screen.rotate_to(i*90 % 360)