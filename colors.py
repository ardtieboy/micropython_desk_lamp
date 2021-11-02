import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

pixel_pin = board.D1
num_pixels = 19
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=neopixel.GRBW) # Default is GRBW

button = DigitalInOut(board.D3)
button.direction = Direction.INPUT
button.pull = Pull.UP

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b, 0)


def fire(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 128:
        r = 255
        g = 256+int(pos*2)
        b = 0
    else:
        pos -= 128
        r = 255
        g = 512-(pos*2)-1
        b = 0
    return (r, g, b, 0)
    
def sea(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 128:
        r = 0
        g = 256+int(pos*2)
        b = 255
    else:
        pos -= 128
        r = 0
        g = 512-(pos*2)-1
        b = 255
    return (r, g, b, 0)
    
def forrest(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 128:
        r = 0
        g = 255
        b = 256+int(pos*2)
    else:
        pos -= 128
        r = 0
        g = 255
        b = 512-(pos*2)-1
    return (r, g, b, 0)
    
def pinkie(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 128:
        r = 255
        g = 0
        b = 256+int(pos*2)
    else:
        pos -= 128
        r = 255
        g = 0
        b = 512-(pos*2)-1
    return (r, g, b, 0)

def off():
    return (0, 0, 0, 0)

def white():
    return (255, 255, 255, 0)

def warm():
    return (246, 205, 139, 0)

mode = 0

def rainbow_cycle(j, mode):
    for i in range(num_pixels):
        pixel_index = (i * 256 // num_pixels) + j
        if mode == 0:
            print("OFF")
            pixels[i] = off()
        elif mode == 1:
            print("WHITE")
            pixels[i] = white()
        elif mode == 2:
            print("WARM")
            pixels[i] = warm()
        elif mode ==3:
            print("FIRE")
            pixels[i] = fire(pixel_index & 255)
        elif mode == 4:
            print("SEA")
            pixels[i] = sea(pixel_index & 255)
        elif mode == 5:
            print("PINKIE")
            pixels[i] = pinkie(pixel_index & 255)      
        elif mode == 6:
            print("FORREST")
            pixels[i] = forrest(pixel_index & 255)  
        elif mode == 7:
            print("RAINBOW")
            pixels[i] = wheel(pixel_index & 255)
    pixels.show()

num_modes = 7

while True:
    print("Start")
    for j in range(255):
        print(mode)
        rainbow_cycle(j, mode)  # rainbow cycle with 1ms delay per step
        time.sleep(0.1)
        if not button.value:
            print("Setting mode")
            mode = mode + 1
            mode = mode % 7
            time.sleep(0.2)
    print("Done")
