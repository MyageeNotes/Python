import pyautogui as pa
import time
import random

def action():
        for i in range(10):
            pa.moveTo(random.randint(0,1920),random.randint(0,1080))
            time.sleep(0.05)

        pa.keyDown('winleft')
        pa.keyDown('s')
        pa.keyUp('winleft')
        pa.keyUp('s')
        pa.typewrite('ahahahahahahaha')

action()
