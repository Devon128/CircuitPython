# Write your code here :-)
import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("Make it red!")
dot.brightness=50
while True:
    print("Make it red!")
    dot.fill((255, 0, 0))
    time.sleep(0.5)
dot.brightness=50
    print("Make it green!")
    dot.fill((0, 255, 0))
    time.sleep(0.5)
dot.brightness=50
    print("Make it blue!")
    dot.fill((0, 0, 255))
    time.sleep(0.5)