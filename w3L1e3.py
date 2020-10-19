from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

B = (102,51,0)
b = (0,0,255)
S = (205,133,63)
W = (25, 255, 255)
R = (255, 0, 0)
Y = (255, 255, 255)


image_pixels = [
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, S, S, S, S, S, S, B,
    S, Y, Y, S, S, Y, Y, S,
    S, Y, Y, S, S, Y, Y, S,
    S, S, b, B, B, S, S, S,
    S, b, B, S, S, B, S, S,
    b, b, B, B, B, B, S, S, 
    ]

sense.set_pixels(image_pixels)