import pydirectinput
import time


def run(t):
    pydirectinput.press('right')
        # time.sleep(0.1)
    pydirectinput.keyDown('right')
    time.sleep(t)
    pydirectinput.keyUp('right')


def ms():
    pydirectinput.press(['right','right','space'])
    pydirectinput.press(['up','up','space'])
    time.sleep(0.2)
    run(1.7)

    pydirectinput.press(['ctrl','a'])
    time.sleep(0.6)

    run(1.6)
    time.sleep(0.3)
    pydirectinput.press(['ctrl','s'])

    time.sleep(1.6)
    run(1.55)
    time.sleep(0.3)
    pydirectinput.press('a')
    time.sleep(0.8)

    pydirectinput.press('s')
    time.sleep(1.25)
    pydirectinput.press('r')
    time.sleep(1)
    pydirectinput.press('gs')
    time.sleep(2)
    pydirectinput.press('0')
    time.sleep(0.2)
    pydirectinput.keyDown('x')
    time.sleep(3.5)
    pydirectinput.keyUp('x')
    time.sleep(0.5)
    pydirectinput.press('esc')
    time.sleep(0.3)
    pydirectinput.press('f10')
    time.sleep(3.8)



