import time
import board
import usb_hid
from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Set up keyboard
kbd = Keyboard(usb_hid.devices)

# LED setup, G=Green B=BLUE
ledG = DigitalInOut(board.GP14)
ledB = DigitalInOut(board.GP15)

# LED direction
ledG.direction = Direction.OUTPUT
ledB.direction = Direction.OUTPUT

# Set switch and direction\
switch = []
for x in range(13):
    temp = DigitalInOut(getattr(board,f"GP{x}"))
    temp.switch_to_input(Pull.UP)
    switch.append(temp)
    continue

while True:
    # We could also do "led.value = not switch.value"!
    if switch[0].value:
        ledB.value = False
    else:
        ledB.value = True
        kbd.send(Keycode.F13)
        time.sleep(0.1)
        kbd.release(Keycode.F13)
        
    if switch[1].value:
        ledB.value = False
    else:
        ledB.value = True
        kbd.send(Keycode.F14)
        time.sleep(0.1)
        kbd.release(Keycode.F14)
        
    if switch[2].value:
        ledB.value = False
    else:
        ledB.value = True
        kbd.send(Keycode.F15)
        time.sleep(0.1)
        kbd.release(Keycode.F15)
        
    if switch[3].value:
        ledB.value = False
    else:
        ledB.value = True
        kbd.send(Keycode.F16)
        time.sleep(0.1)
        kbd.release(Keycode.F16)
        
    if switch[4].value:
        ledB.value = False
    else:
        ledB.value = True
        kbd.send(Keycode.F17)
        time.sleep(0.1)
        kbd.release(Keycode.F17)
        
    if switch[5].value:
        ledB.value = False
    else:
        ledB.value = True
        kbd.send(Keycode.F18)
        time.sleep(0.1)
        kbd.release(Keycode.F18)
        
    if switch[6].value:
        ledB.value = False
    else:
        ledB.value = True
        kbd.send(Keycode.F19)
        time.sleep(0.1)
        kbd.release(Keycode.F19)
        
    if switch[7].value:
        ledB.value = False
    else:
        ledB.value = True
        kbd.send(Keycode.SHIFT, Keycode.F13)
        time.sleep(0.1)
        kbd.release(Keycode.SHIFT, Keycode.F13)
        
    if switch[8].value:
        ledB.value = False
    else:
        ledB.value = True
        kbd.send(Keycode.SHIFT, Keycode.F14)
        time.sleep(0.1)
        kbd.release(Keycode.SHIFT, Keycode.F14)
        
    if switch[9].value:
        ledB.value = False
    else:
        ledB.value = True
        kbd.send(Keycode.SHIFT, Keycode.F15)
        time.sleep(0.1)
        kbd.release(Keycode.SHIFT, Keycode.F15)
        
    if switch[10].value:
        ledB.value = False
    else:
        ledB.value = True
        kbd.send(Keycode.SHIFT, Keycode.F16)
        time.sleep(0.1)
        kbd.release(Keycode.SHIFT, Keycode.F16)
        
    if switch[11].value:
        ledB.value = False
    else:
        ledB.value = True
        kbd.send(Keycode.SHIFT, Keycode.F17)
        time.sleep(0.1)
        kbd.release(Keycode.SHIFT, Keycode.F17)
        
    if switch[12].value:
        ledB.value = False
    else:
        ledB.value = True
        kbd.send(Keycode.SHIFT, Keycode.F18)
        time.sleep(0.1)
        kbd.release(Keycode.SHIFT, Keycode.F18)
            
      # debounce delay
    time.sleep(0.1)
