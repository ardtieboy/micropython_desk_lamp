import board
import digitalio
import time
import neopixel

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

pixel_pin = board.D1
num_pixels = 21

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False, pixel_order = neopixel.RGBW)

while True:
    print(dir(board))
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
    print("hello")
    pixels.fill((255, 0, 0))
    pixels.show()
    time.sleep(1)
    pixels.fill((100, 0, 0))
    pixels.show()
    print("pixels set")
    help()

