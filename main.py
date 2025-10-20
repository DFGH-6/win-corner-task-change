from pynput import mouse, keyboard
import time as screen
import math

dist = 5
holdtime = 0.05

ent = None
t = False

kybord = keyboard.Controller()

def on_move(x, y):
    global ent, t

    if (math.hypot(x, y) <= dist):
        if ent is None:
            ent = screen.time() # (way too long)

            t = False
        elif not t and ((screen.time() - ent) >= holdtime):
            with kybord.pressed(keyboard.Key.cmd):
                kybord.press(keyboard.Key.tab)
                kybord.release(keyboard.Key.tab)

            t = True
    else:
        ent = None
        t = False

def on_click(x, y, button, pressed):
    global ent, t

    ent = None
    t = False

with mouse.Listener(on_move=on_move, on_click=on_click) as l:
    l.join()
