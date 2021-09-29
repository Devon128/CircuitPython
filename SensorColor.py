"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
import simpleio
import neopixel
import adafruit_hcsr04


sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D8, echo_pin=board.D9)
# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness = 0.5)


print("Make it blue!!!!!!!7")
angle = 0

while True:
    try:
        angle = sonar.distance
        print((angle,))
        if angle < 5:
            r = 255
            g = 0
            b = 0
        elif angle < 20:
            r = simpleio.map_range(angle, 5, 20, 255, 0)
            g = 0
            b = simpleio.map_range(angle, 5, 20, 0, 255)
        elif angle < 35:
            r = 0
            g = simpleio.map_range(angle, 20, 35, 0, 255)
            b = simpleio.map_range(angle, 20, 35, 255, 0)
        else:
            r = 0
            g = 0
            b = 255





        dot.fill((int(r), int(g), int(b)))
    except RuntimeError:
        print("Retrying!")

    time.sleep(0.1)