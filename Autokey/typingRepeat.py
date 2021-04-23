import pyautogui as pa
import time

def action():
    for i in range (5):
        print( 5 - i )
        time.sleep(1)

    for i in range(10):
        pa.typewrite('aiueo')
        pa.typewrite('\t\n\n')

action()
