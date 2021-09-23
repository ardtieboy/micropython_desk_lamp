import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

pixel_pin = board.D1
num_pixels = 19
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=neopixel.GRBW) # Default is GRBW

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



def rainbow_cycle(j, mode):
    for i in range(num_pixels):
        pixel_index = (i * 256 // num_pixels) + j
        if mode == 1:
            print("F")
            pixels[i] = fire(pixel_index & 255)
        elif mode == 0:
            print("W")
            pixels[i] = wheel(pixel_index & 255)
    pixels.show()

mode = 1

while True:
    print("Start")
    for j in range(255):
        print(mode)
        rainbow_cycle(j, mode)  # rainbow cycle with 1ms delay per step
        time.sleep(0.1)
        if not button.value:
            print("Setting mode")
            mode = mode + 1
            mode = mode % 2
            time.sleep(1)
    print("Done")
