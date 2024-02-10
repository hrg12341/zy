import random
import pyautogui
import cv2
import pydirectinput
import time
import easyocr
reader = easyocr.Reader(['ch_sim'])
textValue = "取的物"

location = [
    ['down', 2],     #第一张
    ['down', 1],     #第二张
    ['down', 0],     #第三张
    ['down', 0],     #第四张
    ['down', 3]      #第五张
]


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
    screenshot = pyautogui.screenshot(region=(1480, 305, 295, 35))
    screenshot.save("png/image.png")
    result = (str)(reader.readtext("png/image.png", detail=0))

    if(textValue in result):
        time.sleep(3)

    time.sleep(0.28)


def chooseDown(arr):
    pydirectinput.press(arr[0], arr[1], random.uniform(0.08, 0.11))
    time.sleep(0.1)


def ms():
    # 上buff
    # pydirectinput.press(['right','right','space'])
    # pydirectinput.press(['up','up','space'])
    # time.sleep(0.2)
    chooseDown(location[0])

    run(1.7)

    # 第一张图
    pydirectinput.press(['ctrl','a'])
    time.sleep(0.6)
    # pydirectinput.press('down')
    chooseDown(location[1])
    time.sleep(0.2)
    run(0.94)
    listener()


    #第二张图
    time.sleep(0.2)
    run(0.98)
    chooseDown(location[2])

    pydirectinput.press(['ctrl','s'])
    time.sleep(1.5)


    run(0.98)
    listener()


    #第三张图
    # print("第三张图")
    time.sleep(0.2)
    run(0.6)
    pydirectinput.press(['alt','s'])
    time.sleep(1.23)
    chooseDown(location[3])

    run(1.55)
    listener()

    #第四张图
    # print("第四张图")
    time.sleep(0.2)
    run(0.7)
    pydirectinput.press(['ctrl','a'])
    time.sleep(1.6)
    chooseDown(location[4])

    run(1.05)
    listener()
    #Boss
    run(random.uniform(0.5,0.88))
    pydirectinput.press('w')
    time.sleep(0.3)
    pydirectinput.press('s')

    time.sleep(3)

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
    pydirectinput.press('a')
    time.sleep(0.7)
    chooseDown(location[1])
    run(0.85)
    listener()

    # 第二张图
    run(0.34)
    # time.sleep(0.3)
    pydirectinput.press('a')
    time.sleep(1)
    chooseDown(location[2])
    run(1.21)
    listener()

    #第三张图
    run(0.46)
    pydirectinput.press('q')
    time.sleep(0.45)
    chooseDown(location[3])
    run(1.13)
    listener()

    #第四张图
    run(0.25)
    time.sleep(0.1)
    chooseDown(location[4])
    pydirectinput.press("t")
    time.sleep(0.45)
    run(1.16)
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
    pydirectinput.press(['right', 'right', 'space'])
    time.sleep(0.6)

    run(1.68)

     # 第一张图
    pydirectinput.press('s')
    time.sleep(0.7)

    run(1.78)

    # 第二张图
    # time.sleep(0.3)
    pydirectinput.press('s')
    time.sleep(1)

    run(1.95)

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
    run(0.63)
    pydirectinput.press('a')
    time.sleep(0.36)

    chooseDown(location[4])

    run(1.31)
    listener()

    #Boss
    run(random.uniform(0.4,0.6))
    pydirectinput.press('a')
    time.sleep(0.4)
    pydirectinput.press(['right','z'])
    time.sleep(0.3)
    pydirectinput.press('r')
    time.sleep(3)

    autow(2.52)



def fengfa():
    # 上buff
    pydirectinput.press(['right', 'right', 'space'])
    time.sleep(0.58)
    # pydirectinput.press('down')
    # pydirectinput.press('g')

    run(1.43)

    # 第一张图
    pydirectinput.press('alt')
    chooseDown(location[1])
    run(1.06)

    listener()

    # 第二张图
    run(0.618)
    pydirectinput.press('s')
    time.sleep(1.2)
    pydirectinput.press('g')
    chooseDown(location[2])
    run(0.86)
    listener()

    # 第三张图
    run(0.57)
    pydirectinput.press('ctrl')
    pydirectinput.press('g')
    time.sleep(0.07)
    chooseDown(location[3])
    run(0.98)
    listener()

    # 第四张图
    run(0.6)
    chooseDown(location[4])
    time.sleep(0.09)
    pydirectinput.press('q')
    time.sleep(0.47)

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
    run(0.68)
    chooseDown(location[2])

    pydirectinput.press('q')
    time.sleep(0.88)

    run(0.98)
    listener()

    # 第三张图
    # print("第三张图")

    time.sleep(0.2)
    chooseDown(location[3])
    time.sleep(0.1)
    run(0.6)
    pydirectinput.press(['f'])
    time.sleep(0.23)


    # pydirectinput.press('down')

    run(1.15)
    listener()

    # 第四张图
    # print("第四张图")
    time.sleep(0.2)
    run(0.6)
    pydirectinput.press('h')
    time.sleep(2.4)
    chooseDown(location[4])

    run(0.85)
    listener()
    # Boss
    run(random.uniform(0.25, 0.42))
    pydirectinput.press('r')
    time.sleep(1.3)
    pydirectinput.press('d')
    time.sleep(0.5)
    pydirectinput.press('s')

    time.sleep(1)

    autow(2.44)

