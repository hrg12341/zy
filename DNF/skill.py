import random

import pydirectinput
import time


def run(t):
    pydirectinput.press('right')
        # time.sleep(0.1)
    pydirectinput.keyDown('right')
    time.sleep(t)
    pydirectinput.keyUp('right')


# 捡东西
def autow():
    # 捡东西
    pydirectinput.press('0')
    time.sleep(0.2)
    pydirectinput.keyDown('x')
    time.sleep(4.2)
    pydirectinput.keyUp('x')
    time.sleep(0.8)
    pydirectinput.press('esc')
    time.sleep(0.3)


def ms():
    # 上buff
    pydirectinput.press(['right','right','space'])
    pydirectinput.press(['up','up','space'])
    time.sleep(0.2)

    run(1.5)
    # 第一张图
    pydirectinput.press(['ctrl','a'])
    time.sleep(0.6)

    run(1.4)
    #第二张图
    # time.sleep(0.3)
    pydirectinput.press(['ctrl','s'])
    time.sleep(1.6)

    run(1.115)

    # time.sleep(0.3)

    #第三张图
    pydirectinput.press('a')
    time.sleep(0.8)
    pydirectinput.press('f')
    time.sleep(0.78)
    pydirectinput.press('h')
    time.sleep(5)

    autow()


def huahua():
    # 上buff
    pydirectinput.press(['right', 'right', 'space'])
    pydirectinput.press(['up', 'up', 'space','down','down'])
    time.sleep(0.2)


    run(1.1)
    # 第一张图
    pydirectinput.press('a')
    time.sleep(0.6)
    pydirectinput.press("space")
    time.sleep(0.3)

    run(1.04)
    # 第二张图
    # time.sleep(0.3)
    pydirectinput.press('d')
    time.sleep(1)

    run(0.89)

    pydirectinput.press('s')
    time.sleep(0.6)
    pydirectinput.press(['right','space'])
    time.sleep(0.5)

    pydirectinput.press('y')
    time.sleep(7)

    autow()

def axl():
    # 上buff
    pydirectinput.press(['right', 'right', 'space'])
    pydirectinput.press(['up', 'up', 'space'])
    time.sleep(0.3)
    pydirectinput.press('alt')
    pydirectinput.keyDown("down")
    time.sleep(0.2)
    pydirectinput.keyUp("down")
    time.sleep(0.1)

    run(1.3)
    # 第一张图
    pydirectinput.press('q')
    time.sleep(0.6)

    run(1.2)
    # 第二张图
    # time.sleep(0.3)
    pydirectinput.press('e')
    time.sleep(1)
    pydirectinput.press('e')
    time.sleep(0.2)

    run(1.7)

    pydirectinput.press('a')
    time.sleep(0.6)
    # pydirectinput.press(['right','space'])
    # time.sleep(0.5)

    pydirectinput.press('y')
    time.sleep(1.6)
    pydirectinput.press('r')
    time.sleep(0.7)
    pydirectinput.press("s")
    time.sleep(0.3)
    pydirectinput.press('g')
    time.sleep(3)

    autow()


def lvren():
    # 上buff
    pydirectinput.press(['right', 'right', 'space'])
    time.sleep(0.6)

    run(0.98)
    # 第一张图
    pydirectinput.press('g')
    time.sleep(0.7)

    run(1.03)
    # 第二张图
    # time.sleep(0.3)
    pydirectinput.press('f')
    time.sleep(0.5)

    run(1.16)

    pydirectinput.press('s')
    time.sleep(0.84)
    # pydirectinput.press(['right','space'])
    # time.sleep(0.5)

    pydirectinput.press('q')
    time.sleep(0.4)
    pydirectinput.press('alt')
    time.sleep(random.uniform(0.2,0.35))
    pydirectinput.press('r')

    time.sleep(2.6)

    autow()


def naima():
    # 上buff
    pydirectinput.press(['right', 'right', 'space'])
    pydirectinput.press(['up', 'up', 'space','down','down'])
    time.sleep(0.6)

    run(1.17)
    # 第一张图
    pydirectinput.press('a')
    time.sleep(0.7)

    run(1.24)
    # 第二张图
    # time.sleep(0.3)
    pydirectinput.press('a')
    time.sleep(1)

    run(1.59)
    time.sleep(0.12)

    pydirectinput.press('d')
    time.sleep(0.44)
    pydirectinput.press(['e','r','w'])
    time.sleep(1)
    # pydirectinput.press('q')
    time.sleep(3.6)

    autow()


def nq():
    # 上buff
    pydirectinput.press(['right', 'right', 'space'])
    time.sleep(0.6)

    run(1.48)

     # 第一张图
    pydirectinput.press('s')
    time.sleep(0.7)

    run(1.58)

    # 第二张图
    # time.sleep(0.3)
    pydirectinput.press('s')
    time.sleep(1)

    run(1.75)

    pydirectinput.press('a')
    time.sleep(0.85)
    pydirectinput.press('s')
    time.sleep(0.5)
    pydirectinput.press('alt')
    time.sleep(0.4)
    pydirectinput.press('y')
    # time.sleep(0.44)
    # pydirectinput.press(['e','r','w'])
    time.sleep(9)


    autow()


def zhaohuan():
    # 上buff

    pydirectinput.press(['right', 'space'])
    time.sleep(1.3)
    pydirectinput.press(['right', 'right', 'space'])
    time.sleep(0.6)
    pydirectinput.press(['space','ctrl'])
    time.sleep(0.1)
    run(1.48)

     # 第一张图
    pydirectinput.press('a')
    time.sleep(0.7)

    run(1.44)

    # 第二张图
    # time.sleep(0.3)
    pydirectinput.press('a')
    time.sleep(1.2)

    run(1.61)

    pydirectinput.press('a')
    time.sleep(0.65)
    pydirectinput.press('alt')
    time.sleep(0.5)
    pydirectinput.press('q')
    time.sleep(0.2)
    pydirectinput.press(['right','z'])
    time.sleep(0.67)

    pydirectinput.press('ctrl')
    time.sleep(0.44)
    pydirectinput.press('a')
    # pydirectinput.press(['e','r','w'])
    time.sleep(3.0)


    autow()


def fengfa():
    # 上buff
    pydirectinput.press(['right', 'right', 'space'])
    time.sleep(0.58)
    pydirectinput.press('down')
    pydirectinput.press('g',2,0.2)

    run(0.66)

    # 第一张图
    pydirectinput.press('q')
    time.sleep(0.58)
    pydirectinput.press('s')
    time.sleep(0.7)

    pydirectinput.press('g',2)

    run(0.88)

    # 第二张图
    # time.sleep(0.3)
    pydirectinput.press('a')
    time.sleep(0.87)
    pydirectinput.press('alt')
    time.sleep(0.57)

    run(1.15)
    pydirectinput.press('g')

    pydirectinput.press('q')
    time.sleep(0.45)
    pydirectinput.press('w')
    time.sleep(1.49)
    pydirectinput.press('r')
    time.sleep(0.4)
    pydirectinput.press('y')
    time.sleep(3.44)
    sk = ['a',['q','ctrl'],'d','g','h']

    for i in sk:
        pydirectinput.press(i)
        time.sleep(random.uniform(0.27, 0.40))

    time.sleep(5)
    autow()

def pld():
    # 上buff
    pydirectinput.press(['right', 'right', 'space'])
    time.sleep(0.6)

    run(1.6)
    # 第一张图
    pydirectinput.press('q')
    time.sleep(0.7)

    run(1.26)
    # 第二张图
    # time.sleep(0.3)
    pydirectinput.press('d')
    time.sleep(0.5)

    run(0.97)

    pydirectinput.press(['space'])
    time.sleep(0.4)
    pydirectinput.press('h')
    time.sleep(2.25)
    pydirectinput.press('f')
    time.sleep(0.4)
    run(0.28)
    pydirectinput.press('left')

    pydirectinput.press('r')
    time.sleep(1.35)
    pydirectinput.press('w')
    time.sleep(0.3)
    pydirectinput.press('e')
    time.sleep(0.8)
    pydirectinput.press("ctrl")
    time.sleep(0.31)
    pydirectinput.press("s")

    time.sleep(3.6)

    autow()

def ndy():
    # 女弹药
    # 上buff
    pydirectinput.press(['right', 'right', 'space', 'right'])
    time.sleep(0.38)
    # pydirectinput.press('down')
    # pydirectinput.press('g')

    run(1.79)

    # 第一张图
    pydirectinput.press('a')
    time.sleep(0.48)

    pydirectinput.keyDown('right')
    time.sleep(0.22)
    pydirectinput.press('c')
    time.sleep(random.uniform(0.45, 0.12))
    pydirectinput.press('c')
    time.sleep(0.36)
    pydirectinput.keyUp('right')
    # run(1.76)

    # 第二张图
    run(0.738)
    pydirectinput.press(['c','d'])
    time.sleep(0.36)
    # run(1.81)
    pydirectinput.keyDown('right')
    time.sleep(0.22)
    pydirectinput.press('c')
    time.sleep(random.uniform(0.47, 0.62))
    pydirectinput.press('c')
    time.sleep(random.uniform(0.27, 0.32))
    pydirectinput.press('c')
    time.sleep(0.314)
    pydirectinput.keyUp('right')

    # 第三张图
    run(0.396)
    pydirectinput.press('w')
    time.sleep(random.uniform(0.2,0.27))
    # run(1.78)
    pydirectinput.press('g')
    time.sleep(0.22)
    pydirectinput.press('e')
    time.sleep(random.uniform(0.67, 0.72))
    pydirectinput.press('y')
    time.sleep(0.41)
    pydirectinput.press('h')

    time.sleep(8)
    autow()