import pyautogui as pa
import time

for i in range(100):
    x, y = pa.position()
    print('\r{},{}{}'.format(x, y, ' '*5), end='')
    time.sleep(0.1)
