import pyautogui
import pydirectinput
import mouse
import autoit
import os
from pynput.keyboard import Key, Listener
import threading
import time
import random

running = False
thread = None

def click_cookie():

    while running:
        try:
            location = list(pyautogui.locateAllOnScreen('chip.png', confidence=0.8))
            #Point(x=756, y=194)
            #Point(x=1155, y=726)
            autoit.mouse_down()
            for loc in random.sample(location, 3):
                if loc.left > 756 and loc.left <1155:
                    if loc.top > 194 and loc.top < 726:
                        autoit.mouse_move(loc.left, loc.top, speed=4)
                        #autoit.mouse_click()
            autoit.mouse_up()
        except Exception as e:
            print(f"{e}")

def threaders():
    global running

    if not running:
        running = not running
        thread = threading.Thread(target=click_cookie)
        thread.start()
        return
    
    if running:
        running = not running
        thread.join()

def on_press(key):
    try:
        if key.char == 'q':
            print(key)
            threaders()
        if key.char == 'a':
            pass
    except:
        pass

with Listener(on_press=on_press) as listener:
    listener.join() 

