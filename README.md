# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [DistanceSensor](#DistanceSensor)
---

## Hello_CircuitPython

### Description & Code
I had to control the neo pixel to make it change colors.

[Here's the code](https://github.com/Devon128/CircuitPython/blob/main/HelloCircuitPython.py)


### Evidence
Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person.




## CircuitPython_Servo

### Description & Code

I had to make a 180 Servo slowly sweep back and forth between 0 and 180.This is for the future me or the new engineering students in case you would ever need to know how to get a servo to sweep back and forth your coode should look somewhat like the one below.

```python
while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5):  # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)

```

### Evidence
![description](https://github.com/elynch78/Metro-Express/blob/main/Images/gif-servo.gif?raw=true)

Image credit of Ellen(https://github.com/elynch78)
### Wiring

### Reflection




## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection





## DistanceSensor

### Description & Code

```python
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

```

### Evidence

### Wiring

### Reflection

I learned as much about VScode and Git, as I did about the sensors!
