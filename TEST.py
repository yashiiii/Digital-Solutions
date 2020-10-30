from sense_hat import SenseHat 

sense = SenseHat()
sense.clear()


B = (0,0,0)
W = (255,255,255)



image_pixels = [
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, W, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B, 
    ]

sense.set_pixels(image_pixels)