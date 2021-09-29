from digitalio import DigitalInOut, Direction, Pull
import time
import board

interrupter = DigitalInOut(board.D7)
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP

counter = 0

photo = False
state = False

max = 4
start = time.monotonic()


time.sleep(3)
print("I'm Alive!")

while True:
    photo = interrupter.value # this saves the value of pin d7, if you've interupted it
    if photo and not state:  # if this is the FIRST time the interupter detects an object
            counter += 1
    state = photo

    remaining = max - time.monotonic() # this is the 4 subtracted by the current time

    if remaining <= 0:
        print("Interrupts:  ", str(counter))
        max = time.monotonic() + 4
        counter = 0