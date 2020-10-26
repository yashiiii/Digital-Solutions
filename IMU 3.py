from sense_hat import SenseHat

sense = SenseHat()
sense.clear()


red = (255,0,0)


while True:
    
    a = sense.get_accelerometer_raw()
    x = a["x"]
    y = a["y"]
    z = a["z"]
    
    x = abs(x)
    y = abs(y)
    z = abs(z)
    
    if x > 1 or y > 1 or z > 1:
        sense.clear(red)
        
    else:
        sense.clear()
        
        
    
    



    
    
    
    
