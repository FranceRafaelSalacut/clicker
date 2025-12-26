from pynput import keyboard
import time
from icecream import ic
import threading
import os
import pyautogui
import autoit

ic.disable()
run = False

def run_thread(bool):
    global thread

    if not bool:
        ic("Stopping")
        thread.join()
        return
    
    thread = threading.Thread(target=auto_play)
    os.system("cls")
    ic("Starting")
    thread.start()

def auto_play():
    while run:
        #time.sleep(0.1)
        x = None
        try:
            upgrade = list(pyautogui.locateAllOnScreen('images/up_ar.png', confidence=0.8))
            ic(len(upgrade))
        except Exception as e:
            ic()
            ic(e)
            upgrade = None
            pass

        try:
            coin_one = list(pyautogui.locateAllOnScreen('images/coin.png', confidence=0.8))
            ic(len(coin_one))
        except Exception as e:
            ic()
            ic(e)
            coin_one = None
            pass

        try:
            coin_two = list(pyautogui.locateAllOnScreen('images/coin_two.png', confidence=0.8))
            ic(len(coin_two))
        except Exception as e:
            ic()
            ic(e)
            coin_two = None
            pass

        try:
            coin_three = list(pyautogui.locateAllOnScreen('images/coin_three.png', confidence=0.8))
            ic(len(coin_three))
        except Exception as e:
            ic()
            ic(e)
            coin_three = None
            pass

        try:
            close = list(pyautogui.locateAllOnScreen('images/close.png', confidence=0.8))
            ic(len(close))
        except Exception as e:
            ic()
            ic(e)
            close = None
            pass
        
        try:
            box = list(pyautogui.locateAllOnScreen('images/box.png', confidence=0.8))
            ic(len(box))
        except Exception as e:
            ic()
            ic(e)
            box = None
            pass

        try:
            afly = list(pyautogui.locateAllOnScreen('images/flyy.png', confidence=0.8))
            ic(len(afly))
        except Exception as e:
            ic()
            ic(e)
            afly = None
            pass

        try:
            afly = list(pyautogui.locateAllOnScreen('images/open.png', confidence=0.8))
            ic(len(afly))
        except Exception as e:
            ic()
            ic(e)
            afly = None
            pass
        
        if afly:
            ic()
            x = afly[0]
            autoit.mouse_move(x.left+15, x.top+15, speed=0)
            autoit.mouse_click()
        elif coin_three:
            ic()
            x = coin_three[0]
            autoit.mouse_move(x.left+15, x.top+15, speed=0)
            autoit.mouse_click()
        elif coin_two:
            ic()
            x = coin_two[0]
            autoit.mouse_move(x.left+15, x.top+15, speed=0)
            for x in range(0,35):
                autoit.mouse_click()
        elif coin_one:
            ic()
            x = coin_one[0]
            autoit.mouse_move(x.left+15, x.top+15, speed=0)
            autoit.mouse_click()
        elif box:
            ic()
            x = box[0]
            autoit.mouse_move(x.left+22, x.top+22, speed=0)
            autoit.mouse_click()
        elif upgrade:
            ic()
            x = upgrade[0]
            autoit.mouse_move(x.left+15, x.top+15, speed=0)
            autoit.mouse_click()
            time.sleep(0.1)
        elif close:
            ic()
            x = close[0]
            autoit.mouse_move(x.left+15, x.top+15, speed=0)
            autoit.mouse_click()

def on_press(key):
    global run
    try:
        if key.char == 'q':
            if not run:
                run = not run
                run_thread(True)
                return

            if run:
                run = not run
                run_thread(False)
                return
        else:
            print("no")
    except Exception as e:
        ic(e)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join() 

