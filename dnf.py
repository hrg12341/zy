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
    time.sleep(3.2)
    pydirectinput.keyUp('x')
    time.sleep(0.8)
    pydirectinput.press('esc')
    time.sleep(0.3)
    pydirectinput.press('f10')
    time.sleep(3.3)

def ms():
    # 上buff
    pydirectinput.press(['right','right','space'])
    pydirectinput.press(['up','up','space'])
    time.sleep(0.2)

    run(1.7)
    # 第一张图
    pydirectinput.press(['ctrl','a'])
    time.sleep(0.6)

    run(1.6)
    #第二张图
    # time.sleep(0.3)
    pydirectinput.press(['ctrl','s'])
    time.sleep(1.6)

    run(1.55)

    # time.sleep(0.3)

    #第三张图
    pydirectinput.press('a')
    time.sleep(0.8)

    pydirectinput.press('h')
    time.sleep(5)

    autow()


def huahua():
    # 上buff
    pydirectinput.press(['right', 'right', 'space'])
    pydirectinput.press(['up', 'up', 'space','down'])
    time.sleep(0.2)


    run(1.3)
    # 第一张图
    pydirectinput.press('a')
    time.sleep(0.6)

    run(1.2)
    # 第二张图
    # time.sleep(0.3)
    pydirectinput.press('d')
    time.sleep(1)

    run(1)

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
    pydirectinput.press(['up', 'up', 'space','down','down'])
    pydirectinput.press('alt')
    time.sleep(0.2)


    run(1.4)
    # 第一张图
    pydirectinput.press('q')
    time.sleep(0.6)

    run(1.3)
    # 第二张图
    # time.sleep(0.3)
    pydirectinput.press('e')
    time.sleep(1)

    run(2.1)

    pydirectinput.press('a')
    time.sleep(0.6)
    # pydirectinput.press(['right','space'])
    # time.sleep(0.5)

    pydirectinput.press('y')
    time.sleep(1.6)
    pydirectinput.press('r')
    time.sleep(1)
    pydirectinput.press('g')
    time.sleep(3)

    autow()


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
    time.sleep(1)

    run(1.56)

    pydirectinput.press('s')
    time.sleep(0.44)
    # pydirectinput.press(['right','space'])
    # time.sleep(0.5)

    pydirectinput.press('alt')
    time.sleep(0.5)
    pydirectinput.press('r')
    time.sleep(1)
    pydirectinput.press('q')
    time.sleep(2.6)

    autow()


def naima():
    # 上buff
    pydirectinput.press(['right', 'right', 'space'])
    pydirectinput.press(['up', 'up', 'space','down','down'])
    time.sleep(0.6)

    run(1.37)
    # 第一张图
    pydirectinput.press('a')
    time.sleep(0.7)

    run(1.44)
    # 第二张图
    # time.sleep(0.3)
    pydirectinput.press('a')
    time.sleep(1)

    run(1.86)
    pydirectinput.press('s')
    time.sleep(0.65)

    pydirectinput.press('d')
    time.sleep(0.44)
    pydirectinput.press(['e','r','w'])
    time.sleep(1)
    # pydirectinput.press('q')
    time.sleep(3.6)

    autow()




