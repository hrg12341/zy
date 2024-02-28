import random
import pyautogui
import cv2
import main
import pydirectinput
import time
import easyocr
reader = easyocr.Reader(['ch_sim'])
textValue = "取的物"

computerlo = main.computerlo
location = main.location


def run(t):
    pydirectinput.press('right')
        # time.sleep(0.1)
    pydirectinput.keyDown('right')
    time.sleep(t)
    pydirectinput.keyUp('right')


# 捡东西
def autow(second):
    # 捡东西
    pydirectinput.press('0')
    time.sleep(0.2)
    pydirectinput.keyDown('x')
    time.sleep(second)
    pydirectinput.keyUp('x')
    time.sleep(2.1)
    pydirectinput.press('esc')
    time.sleep(1.4)
    pydirectinput.press('esc')
    time.sleep(0.3)

def listener():
    time.sleep(0.2)
    screenshot = pyautogui.screenshot(region=(computerlo,305,295,35))
    screenshot.save("png/image.png")
    result = (str)(reader.readtext("png/image.png", detail=0))

    if(textValue in result):
        time.sleep(3)

    time.sleep(0.18)


def chooseDown(arr):
    ty = 'down'
    if(arr < 0): ty = 'up'
    if(arr!=0):
        pydirectinput.press(ty, abs(arr), random.uniform(0.09, 0.13))
        time.sleep(0.1)


def ms():
    # 上buff
    pydirectinput.press(['right','right','space'])
    # pydirectinput.press(['up','up','space'])
    # time.sleep(0.2)
    chooseDown(location[0])

    run(1.77)

    # 第一张图
    pydirectinput.press(['ctrl','a'])
    time.sleep(0.6)
    # pydirectinput.press('down')
    chooseDown(location[1])
    time.sleep(0.2)
    run(0.96)
    listener()


    #第二张图
    time.sleep(0.2)
    run(0.82)
    chooseDown(location[2])

    pydirectinput.press(['ctrl','s'])
    time.sleep(1.5)
    pydirectinput.press("8")

    run(1.28)
    listener()


    #第三张图
    # print("第三张图")
    time.sleep(0.2)
    run(0.66)
    pydirectinput.press(['alt','s'])
    time.sleep(1.23)
    chooseDown(location[3])
    pydirectinput.press("8")

    run(1.07)
    listener()

    #第四张图
    # print("第四张图")
    time.sleep(0.2)
    run(0.72)
    pydirectinput.press(['ctrl','a'])
    time.sleep(1.3)
    chooseDown(location[4])
    pydirectinput.press("8")

    run(1.05)
    listener()
    #Boss

    run(random.uniform(0.3,0.52))
    pydirectinput.press('w')
    time.sleep(0.3)
    pydirectinput.press('d')

    time.sleep(2.6)
    pydirectinput.press("8")

    autow(2.44)


def huahua():
    # 上buff
    pydirectinput.press(['right', 'right', 'space'])
    pydirectinput.press(['up', 'up', 'space','down','down'])
    time.sleep(0.2)


    run(1.3)
    # 第一张图
    pydirectinput.press('a')
    time.sleep(0.6)
    pydirectinput.press("space")
    time.sleep(0.3)

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
    pydirectinput.press(['up', 'up', 'space'])
    time.sleep(0.3)
    pydirectinput.press('alt')
    pydirectinput.keyDown("down")
    time.sleep(0.2)
    pydirectinput.keyUp("down")
    time.sleep(0.1)

    run(1.5)
    # 第一张图
    pydirectinput.press('q')
    time.sleep(0.6)

    run(1.4)
    # 第二张图
    # time.sleep(0.3)
    pydirectinput.press('e')
    time.sleep(1)

    run(1.9)

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
    chooseDown(location[0])
    pydirectinput.press(['right', 'right', 'space'])
    time.sleep(0.6)

    run(1.2)
    # 第一张图
    pydirectinput.press('s')
    time.sleep(0.7)
    chooseDown(location[1])
    run(0.99)
    listener()

    # 第二张图
    # time.sleep(0.3)
    run(0.15)
    chooseDown(location[2])
    pydirectinput.press('down', 2, 0.08)
    pydirectinput.press('f')
    time.sleep(0.5)
    pydirectinput.press('up',2,0.08)
    time.sleep(0.1)
    run(1.42)
    listener()

    # 第三张图
    run(0.28)
    pydirectinput.press('g')
    time.sleep(0.64)
    chooseDown(location[3])
    run(1.38)
    listener()

    #第四张图
    run(0.45)
    time.sleep(0.1)
    chooseDown(location[4])
    pydirectinput.press("w")
    time.sleep(0.45)
    run(1.06)
    listener()

    #Boss
    run(0.52)
    pydirectinput.press('r')

    time.sleep(1.96)

    autow(2.43)


def naima():
    # 上buff
    pydirectinput.press(['right', 'right', 'space'])
    # pydirectinput.press(['up', 'up', 'space','down','qdown'])
    time.sleep(0.6)

    run(1.37)
    # 第一张图
    chooseDown(location[1])
    pydirectinput.press('a')
    time.sleep(0.7)

    run(0.92)
    listener()

    # 第二张图
    run(0.34)
    # time.sleep(0.3)
    chooseDown(location[2])
    pydirectinput.press('a')
    time.sleep(1)

    run(1.24)
    listener()

    #第三张图
    run(0.46)
    chooseDown(location[3])
    pydirectinput.press('q')
    time.sleep(0.45)
    run(1.18)
    listener()

    #第四张图
    run(0.25)
    time.sleep(0.1)
    chooseDown(location[4])
    pydirectinput.press("t")
    time.sleep(0.45)
    run(1.24)
    listener()

    #Boss
    run(0.35)
    pydirectinput.press('d')
    time.sleep(0.44)
    pydirectinput.press(['s'])
    time.sleep(1)
    # pydirectinput.press('q')
    time.sleep(1.6)

    autow(2.41)


def nq():
    # 上buff
    chooseDown(location[0])
    pydirectinput.press(['right', 'right', 'space'])
    time.sleep(0.6)

    run(1.18)

     # 第一张图
    chooseDown(location[1])
    pydirectinput.press('s')
    time.sleep(0.7)

    run(1.54)
    listener()

    # 第二张图
    chooseDown(location[2])
    run(0.38)
    pydirectinput.press(['d','q'])
    time.sleep(1.88)
    run(0.43+0.9)
    # pydirectinput.press('s')
    # time.sleep(0.6)
    # run(0.91)
    listener()

    #第三张图
    chooseDown(location[3])
    run(0.31)
    pydirectinput.press('a')
    time.sleep(0.85)
    run(1.53)
    listener()

    #第四张图
    chooseDown(location[4])
    run(0.28)
    pydirectinput.press('s')
    time.sleep(0.8)
    run(1.5)
    listener()

    #Boss
    run(random.uniform(0.3,0.52))
    pydirectinput.press('r')
    time.sleep(0.89)
    pydirectinput.press('s')
    time.sleep(0.71)
    time.sleep(1.1)


    autow(2.1)


def zhaohuan():
    # 上buff
    chooseDown(location[0])
    time.sleep(0.1)

    pydirectinput.press(['right', 'space'])
    time.sleep(1.3)
    pydirectinput.press(['right', 'right', 'space'])
    time.sleep(0.6)
    pydirectinput.press(['space','ctrl'])
    time.sleep(0.1)
    run(1.78)

     # 第一张图
    pydirectinput.press('a')
    time.sleep(0.33)
    chooseDown(location[1])

    run(0.84)
    listener()

    # 第二张图
    chooseDown(location[2])
    time.sleep(0.1)
    run(1.41)
    pydirectinput.press('ctrl')
    time.sleep(0.34)
    
    pydirectinput.press('a')
    run(0.37)
    listener()


    #第三张图
    run(0.83)
    time.sleep(0.23)
    chooseDown(location[3])
    pydirectinput.press('a')
    time.sleep(0.41)

    run(1.3)
    listener()

    #第4张图
    chooseDown(location[4])
    run(0.63)
    pydirectinput.press('a')
    time.sleep(0.36)

    run(1.31)
    listener()

    #Boss
    run(random.uniform(0.4,0.6))
    pydirectinput.press('a')
    time.sleep(0.4)
    pydirectinput.press(['right','z'])
    time.sleep(0.3)
    pydirectinput.press('r')
    time.sleep(6)

    autow(2.52)



def fengfa():
    # 上buff
    chooseDown(location[0])
    pydirectinput.press(['right', 'right', 'space'])
    time.sleep(0.58)
    # pydirectinput.press('down')
    # pydirectinput.press('g')

    run(1.53)

    # 第一张图
    pydirectinput.press('alt')
    chooseDown(location[1])
    run(1.06)

    listener()

    # 第二张图
    run(0.618)
    chooseDown(location[2])
    pydirectinput.press('s')
    time.sleep(1.2)
    pydirectinput.press('g')
    time.sleep(0.1)
    pydirectinput.press('q')
    time.sleep(0.1)
    pydirectinput.press("8")
    run(0.46)
    listener()

    # 第三张图
    chooseDown(location[3])
    run(0.37)
    pydirectinput.press('ctrl')
    pydirectinput.press('g')
    pydirectinput.press("8")
    time.sleep(0.07)

    run(1.18)
    listener()

    # 第四张图
    chooseDown(location[4])
    run(0.6)

    time.sleep(0.09)
    pydirectinput.press('q')
    time.sleep(0.47)
    pydirectinput.press("8")
    pydirectinput.press('g')

    # pydirectinput.press('down')

    time.sleep(0.08)
    run(0.68)
    listener()

    #Boss
    run(0.7)

    pydirectinput.press('g')
    pydirectinput.press('y')
    time.sleep(5.56)
    pydirectinput.press('alt')
    time.sleep(0.32)
    autow(2.45)

def pld():
    # 上buff
    chooseDown(location[0])
    time.sleep(0.1)
    pydirectinput.press(['right','right','space'])
    pydirectinput.press('down')

    run(1.4)

    # 第一张图
    pydirectinput.press('space')
    time.sleep(0.3)
    pydirectinput.press('ctrl')
    time.sleep(0.4)
    # pydirectinput.press('down')
    chooseDown(location[1])
    time.sleep(0.2)
    run(0.94)
    listener()

    # 第二张图
    time.sleep(0.2)
    run(0.72)
    chooseDown(location[2])

    pydirectinput.press('h')
    time.sleep(2.48)
    pydirectinput.press("8")
    run(0.94)
    listener()

    # 第三张图
    # print("第三张图")

    time.sleep(0.2)
    chooseDown(location[3])
    time.sleep(0.1)
    run(0.6)
    pydirectinput.press(['q'])
    time.sleep(0.83)
    pydirectinput.press("8")

    # pydirectinput.press('down')

    run(1.15)
    listener()

    # 第四张图
    # print("第四张图")
    time.sleep(0.2)
    run(0.6)
    pydirectinput.press('f')
    time.sleep(0.4)
    chooseDown(location[4])
    pydirectinput.press("8")
    run(0.85)
    listener()
    # Boss
    run(random.uniform(0.25, 0.42))
    pydirectinput.press('r')
    time.sleep(1.3)
    pydirectinput.press('d')
    time.sleep(0.5)
    pydirectinput.press('e')
    time.sleep(1.1)
    pydirectinput.press("ctrl")
    time.sleep(0.45)
    pydirectinput.press("s")

    time.sleep(1)

    autow(2.44)
