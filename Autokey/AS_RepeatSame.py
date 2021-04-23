import pyautogui as pa
import time
import random


def arrow(x, y):
    pa.moveTo(x, y)


def tap(after, key, rep=1):
    for x in range(rep):
        for t in range(after):
            print('\r{}:{}{}'.format(key, '◆' * (after - t), ' '*30), end='')
            time.sleep(1)
        pa.keyDown(key)
        time.sleep(random.uniform(0.1, 0.8))
        pa.keyUp(key)
        print('\r{}:Tapped'.format(key, ' ' * 30))


def typing(s):
    pa.typewrite(s)


def action():
    # START
    # Song Select
    tap(5, 'enter')
    # Friend Select
    tap(7, 'f')
    # LiveStart
    tap(7, 'enter')
    time.sleep(5)
    # LIVE
    for n in range(2):
        tap(5, 'l', 6)
        tap(5, 'space')
        tap(5, 'l')
    tap(4, 'l', 5)
    tap(5, 'space')
    time.sleep(15)

    # Result
    tap(1, 'space', 10)
    tap(3, 'o', 2)
    time.sleep(10)


def recover_lp():
    tap(1, 'p')
    tap(1, 'f')
    tap(1, 'q')
    time.sleep(2)
    tap(1, 'o')
    time.sleep(1)


if __name__ == '__main__':
    recover_lp()
    while True:
        for i in range(10):
            action()
        recover_lp()
