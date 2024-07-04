from pynput import keyboard
import autoit
from icecream import ic

down = False

def on_press(key):
    global down
    try:
        if key.char == 'q':
            autoit.mouse_click()
        elif key.char == 'w':
            if down:
                autoit.mouse_up()
            else:
                autoit.mouse_down()
            down = not down
        else:
            pass
    except Exception as e:
        ic(e)


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()