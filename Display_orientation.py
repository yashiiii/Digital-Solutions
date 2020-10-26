from sense_hat import SenseHat 

sense = SenseHat()
sense.clear()

sense.set_rotation(270) 

B = (102,51,0)
b = (0,0,255)
S = (205,133,63)
W = (255, 255, 255)


image_pixels = [
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, S, S, S, S, S, S, B,
    S, S, S, S, S, S, S, S,
    S, W, b, S, S, b, W, S,
    S, S, S, B, B, S, S, S,
    S, S, B, S, S, B, S, S,
    S, S, B, B, B, B, S, S, 
    ]

sense.set_pixels(image_pixels)