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
    time.sleep(0.4)
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

def zbauto():
    pydirectinput.press('8')
    time.sleep(0.1)
    pydirectinput.keyDown('x')
    time.sleep(random.uniform(0.4,0.67))
    pydirectinput.keyUp('x')
    time.sleep(random.uniform(0.33,0.44))


def ms():
    # 上buff
    pydirectinput.press(['right','right','space'])
    # pydirectinput.press(['up','up','space'])
    time.sleep(0.2)
    chooseDown(location[0])

    run(1.57)

    # 第一张图
    pydirectinput.press(['ctrl','a'])
    time.sleep(0.6)
    # pydirectinput.press('down')
    chooseDown(location[1])
    time.sleep(0.2)
    run(0.76)
    listener()


    #第二张图
    time.sleep(0.2)
    run(0.72)
    chooseDown(location[2])

    pydirectinput.press(['ctrl','s'])
    time.sleep(1.5)
    zbauto()

    run(1.12)
    listener()


    #第三张图
    # print("第三张图")
    time.sleep(0.2)
    run(0.62)
    pydirectinput.press(['alt','s'])
    time.sleep(1.23)
    chooseDown(location[3])
    zbauto()

    run(0.99)
    listener()

    #第四张图
    # print("第四张图")
    time.sleep(0.2)
    run(0.52)
    pydirectinput.press(['ctrl','a'])
    time.sleep(1.3)
    chooseDown(location[4])
    zbauto()

    run(0.98)
    listener()
    #Boss

    run(random.uniform(0.3,0.42))
    pydirectinput.press('w')
    time.sleep(0.3)
    pydirectinput.press('d')

    time.sleep(1.4)
    pydirectinput.press('r')
    time.sleep(1.2)
    pydirectinput.press('8')

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
    chooseDown(location[0])
    run(1.2)
    # 第一张图
    pydirectinput.press('q')
    time.sleep(0.7)
    zbauto()
    chooseDown(location[1])
    run(1.28)
    listener()

    # 第二张图
    chooseDown(location[2])
    run(0.18)
    pydirectinput.press('e')
    time.sleep(0.88)
    zbauto()
    run(0.43 + 0.78)
    # pydirectinput.press('s')
    # time.sleep(0.6)
    # run(0.91)
    listener()

    # 第三张图
    chooseDown(location[3])
    run(0.31)
    pydirectinput.press('a')
    time.sleep(0.85)
    zbauto()
    run(1.53)
    listener()

    # 第四张图
    chooseDown(location[4])
    run(0.28)
    pydirectinput.press('q')
    time.sleep(0.8)
    zbauto()
    run(1.5)
    listener()

    # Boss
    run(random.uniform(0.3, 0.52))
    pydirectinput.press('g')
    time.sleep(0.91)
    pydirectinput.press('8')
    time.sleep(1.1)

    autow(2.1)


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
    time.sleep(0.22)
    chooseDown(location[0])

    run(1.17)
    # 第一张图
    chooseDown(location[1])
    pydirectinput.press('a')
    time.sleep(0.75)
    zbauto()

    run(0.92)
    listener()

    # 第二张图
    run(0.46)
    # time.sleep(0.3)
    chooseDown(location[2])
    pydirectinput.press('a')
    time.sleep(1)
    zbauto()
    run(0.96)
    listener()

    #第三张图
    run(0.36)
    chooseDown(location[3])
    pydirectinput.press('q')
    time.sleep(0.45)
    zbauto()
    run(1.028)
    listener()

    #第四张图
    run(0.25)
    time.sleep(0.1)
    chooseDown(location[4])
    pydirectinput.press("t")
    time.sleep(0.45)
    zbauto()
    run(1.04)
    listener()

    #Boss
    run(0.45)
    pydirectinput.press('d')
    time.sleep(0.44)
    pydirectinput.press(['s'])
    time.sleep(1)

    time.sleep(1.6)
    pydirectinput.press('8')
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
    run(1.64)
    listener()

    # 第二张图
    chooseDown(location[2])
    run(0.28)
    pydirectinput.press(['d','q'])
    time.sleep(1.88)
    zbauto()
    time.sleep(0.12)
    run(1.58)
    # pydirectinput.press('s')
    # time.sleep(0.6)
    # run(0.91)
    listener()

    #第三张图
    chooseDown(location[3])
    run(0.31)
    pydirectinput.press('a')
    time.sleep(0.85)
    zbauto()
    time.sleep(0.12)
    run(1.58)
    listener()

    #第四张图
    chooseDown(location[4])
    run(0.28)
    pydirectinput.press('s')
    time.sleep(0.8)
    zbauto()
    time.sleep(0.12)
    run(1.5)
    listener()

    #Boss
    run(random.uniform(0.22,0.38))
    pydirectinput.press(['r','q','q'])
    time.sleep(0.89)
    pydirectinput.press('s')
    time.sleep(0.71)
    pydirectinput.press('8')
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
    run(1.58)

     # 第一张图
    pydirectinput.press('a')
    time.sleep(0.33)
    chooseDown(location[1])
    zbauto()
    run(0.64)
    listener()

    # 第二张图
    chooseDown(location[2])
    time.sleep(0.1)
    run(1.21)
    pydirectinput.press('ctrl')
    time.sleep(0.34)
    
    pydirectinput.press('a')
    time.sleep(0.45)
    zbauto()
    run(0.27)
    listener()


    #第三张图
    run(0.63)
    time.sleep(0.23)
    chooseDown(location[3])
    pydirectinput.press('a')
    time.sleep(0.41)
    zbauto()
    run(1.11)
    listener()

    #第4张图
    chooseDown(location[4])
    run(0.53)
    pydirectinput.press('a')
    time.sleep(0.36)
    zbauto()
    run(1.11)
    listener()

    #Boss
    run(random.uniform(0.3,0.46))
    pydirectinput.press('a')
    time.sleep(0.4)
    pydirectinput.press(['right','z'])
    time.sleep(0.3)
    pydirectinput.press('r')
    time.sleep(3)
    pydirectinput.press('8')
    time.sleep(3)
    autow(2.152)



def fengfa():
    # 上buff
    chooseDown(location[0])
    pydirectinput.press(['right', 'right', 'space'])
    time.sleep(0.58)
    # pydirectinput.press('down')
    # pydirectinput.press('g')

    run(1.23)

    # 第一张图
    pydirectinput.press('alt')
    chooseDown(location[1])
    run(0.88)

    listener()

    # 第二张图
    run(0.518)
    chooseDown(location[2])
    pydirectinput.press('s')
    time.sleep(1.2)
    pydirectinput.press('g')
    time.sleep(0.1)
    pydirectinput.press('q')
    time.sleep(0.1)
    zbauto()
    run(0.44)
    listener()

    # 第三张图
    chooseDown(location[3])
    run(0.31)
    pydirectinput.press('ctrl')
    pydirectinput.press('g')
    time.sleep(0.1)
    zbauto()
    time.sleep(0.07)

    run(0.88)
    listener()

    # 第四张图
    chooseDown(location[4])
    run(0.46)

    time.sleep(0.09)
    pydirectinput.press('q')
    time.sleep(0.47)
    zbauto()
    pydirectinput.press('g')

    # pydirectinput.press('down')

    time.sleep(0.08)
    run(0.58)
    listener()

    #Boss
    run(0.47)

    pydirectinput.press('g')
    time.sleep(0.11)
    pydirectinput.press('ctrl')
    time.sleep(.26)
    pydirectinput.press('e')
    time.sleep(.61)
    pydirectinput.press('y')
    time.sleep(4.26)
    pydirectinput.press('alt')
    time.sleep(0.32)
    pydirectinput.press('8')
    autow(2.45)

def pld():
    # 上buff
    chooseDown(location[0])
    time.sleep(0.1)
    pydirectinput.press(['right','right','space'])

    run(0.98)

    # 第一张图
    pydirectinput.press('space')
    time.sleep(0.3)
    pydirectinput.press('w')
    time.sleep(0.46)
    # pydirectinput.press('down')
    chooseDown(location[1])
    time.sleep(0.2)
    run(0.93)
    listener()

    # 第二张图
    time.sleep(0.2)
    run(0.52)
    chooseDown(location[2])

    pydirectinput.press('h')
    time.sleep(2.48)
    zbauto()
    run(0.74)
    listener()

    # 第三张图
    # print("第三张图")

    time.sleep(0.2)
    chooseDown(location[3])
    time.sleep(0.1)
    run(0.46)
    pydirectinput.press(['q'])
    time.sleep(0.83)
    zbauto()

    # pydirectinput.press('down')

    run(0.95)
    listener()

    # 第四张图
    # print("第四张图")
    time.sleep(0.2)
    run(0.416)
    pydirectinput.press('f')
    time.sleep(0.4)
    chooseDown(location[4])
    pydirectinput.press("8")
    run(0.65)
    listener()
    # Boss
    run(random.uniform(0.25, 0.37))
    pydirectinput.press('y')
    time.sleep(3.04)
    pydirectinput.press('right')
    pydirectinput.keyDown('right')
    time.sleep(0.22)
    pydirectinput.keyUp('right')
    pydirectinput.press('left')
    pydirectinput.press('r')
    time.sleep(1.6)
    pydirectinput.press('d')
    time.sleep(0.5)
    pydirectinput.press('e')
    time.sleep(1.1)
    pydirectinput.press('w')
    time.sleep(0.42)
    pydirectinput.press("ctrl")
    time.sleep(0.45)
    pydirectinput.press('8')
    pydirectinput.press("s")

    time.sleep(1.65)

    autow(2.44)


def ndy():
    # 女弹药
    # 上buff
    chooseDown(location[0])
    pydirectinput.press(['right', 'right', 'space', 'right'])
    time.sleep(0.38)
    # pydirectinput.press('down')
    # pydirectinput.press('g')

    run(1.65)

    # 第一张图
    pydirectinput.press('a')
    time.sleep(0.48)
    chooseDown(location[1])

    pydirectinput.keyDown('right')
    time.sleep(0.22)
    pydirectinput.press('c')
    time.sleep(random.uniform(0.45, 0.12))
    pydirectinput.press('c')
    time.sleep(0.36)
    pydirectinput.keyUp('right')
    # run(1.76)
    listener()

    # 第二张图
    chooseDown(location[2])
    run(0.318)
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
    listener()

    # 第三张图
    chooseDown(location[3])
    run(0.546)
    pydirectinput.press('e')
    time.sleep(random.uniform(0.2,0.27))
    # run(1.78)
    pydirectinput.keyDown('right')
    time.sleep(0.22)
    pydirectinput.press('c')
    time.sleep(random.uniform(0.27, 0.32))
    pydirectinput.press('c')
    time.sleep(0.41)
    pydirectinput.keyUp('right')
    listener()

    # 第四张图
    chooseDown(location[4])
    run(0.639)
    time.sleep(0.09)
    pydirectinput.press('a')
    time.sleep(0.47)
    # run(1.74)
    pydirectinput.keyDown('right')
    time.sleep(0.22)
    pydirectinput.press('c',2,random.uniform(0.47,0.6))
    time.sleep(0.4)
    pydirectinput.keyUp('right')
    listener()

    # Boss
    run(random.uniform(0.21,0.35))

    pydirectinput.press('s')
    time.sleep(0.34)
    pydirectinput.press('f')
    time.sleep(0.32)
    pydirectinput.press('g')
    time.sleep(random.uniform(0.22, 0.32))
    pydirectinput.press('y')
    time.sleep(0.61)
    pydirectinput.press('h')
    time.sleep(9.56)

    autow(2.25)