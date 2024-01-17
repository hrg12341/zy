import pydirectinput
import time


def run(t):
    pydirectinput.press('right')
        # time.sleep(0.1)
    pydirectinput.keyDown('right')
    time.sleep(t)
    pydirectinput.keyUp('right')


# 捡东西
def autow(t):
    # 捡东西
    pydirectinput.press('0')
    time.sleep(0.2)
    pydirectinput.keyDown('x')
    time.sleep(t)
    pydirectinput.keyUp('x')
    time.sleep(0.8)
    pydirectinput.press('esc')
    time.sleep(0.3)
    pydirectinput.press('f10')
    time.sleep(2.9)

def nq():
    # 上buff
    pydirectinput.press(['right', 'right', 'space'])
    time.sleep(0.2)

def lvren():
    # 上buff
    pydirectinput.press(['right', 'right', 'space'])
    time.sleep(0.6)

    run(1.3)
    # 第一张图
    pydirectinput.press('g')
    time.sleep(0.7)

    run(1.36)
    # 第二张图
    # time.sleep(0.3)
    pydirectinput.press('f')
    time.sleep(0.5)

    run(1.56)

    # 第三张图
    pydirectinput.press('s')
    time.sleep(0.84)
    # pydirectinput.press(['right','space'])
    # time.sleep(0.5)

    pydirectinput.press('q')
    time.sleep(0.4)
    pydirectinput.press('alt')
    time.sleep(0.5)
    pydirectinput.press('r')

    time.sleep(2.6)

    autow()