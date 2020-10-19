from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

blue = (0,0,225)
red = (255,0,0)
yellow = (255,255,0)
green = (0,225,0)
cyan = (0,255,255)
magenta = (255,0,255)
black = (0,0,0)
white = (255,225,225)

sense.show_letter("M", red)
sleep(0.5)
sense.show_letter("U", yellow)
sleep(0.5)
sense.show_letter("R", green)
sleep(0.5)
sense.show_letter("T", cyan)
sleep(0.5)
sense.show_letter("A", blue)
sleep(0.5)
sense.show_letter("G", magenta)
sleep(0.5)
sense.show_letter("H", white)
sleep(0.5)
        
        
        