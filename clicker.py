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

def click():
    global running
    while running:
        try:
            location = pyautogui.locateOnScreen('cogtwo.png')
            location = pyautogui.size()
            x = int(location.width/2)
            y = int(location.height/2)
            #pydirectinput.click(x,y, clicks=5)
            autoit.mouse_click("left", x, y, 100, 0)
            print("found")
        except:
            print("error")


def check_thread():
    global running
    global that_thread

    if not running:
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

