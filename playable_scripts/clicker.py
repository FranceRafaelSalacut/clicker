import pyautogui
import pydirectinput
import mouse
import autoit
import os
from pynput.keyboard import Key, Listener
import threading
import time

running = False
that_thread = None
x = 0
y = 0

def click():
    global running
    global x
    global y

    while running:
        autoit.mouse_click("left", x, y, 1, 0)
        print("found")
        time.sleep(0.0001)

def check_thread():
    global running
    global that_thread
    global x 
    global y

    if not running:
        try:
            location = pyautogui.locateOnScreen('cogtwo.png')
            location = pyautogui.size()
            x = int(location.width/2)
            y = int(location.height/2)
            #pydirectinput.click(x,y, clicks=5)
        except:
            print("error")
            return
        print("Starting")
        running = True
        that_thread = threading.Thread(target=click)
        that_thread.start()
        return

    if running:
        print("Stopping")
        running = False
        that_thread.join()
        return


def on_press(key):
    try:
        if key.char == 'q':
            print(key)
            check_thread()
        if key.char == 'a':
            pass
    except:
        pass

size = pyautogui.size()
print(size.width)

with Listener(on_press=on_press) as listener:
    listener.join() 

