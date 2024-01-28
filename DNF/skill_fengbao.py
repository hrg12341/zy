import random
import pyautogui
import cv2
import pydirectinput
import time
from skimage.metrics import structural_similarity as ssim


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
    screenshot.save("png/compare.png")
    image1 = cv2.cvtColor(cv2.imread("png/loc.png"), cv2.COLOR_BGR2GRAY)
    image2 = cv2.cvtColor(cv2.imread("png/compare.png"), cv2.COLOR_BGR2GRAY)

    ssim_value = ssim(image1, image2)
    threshold = 0.79

    if(ssim_value>threshold):
        print("ssim:" + str(ssim_value))
        time.sleep(3)

    time.sleep(0.28)

def ms():
    # 上buff
    pydirectinput.press(['right','right','space'])
    pydirectinput.press(['up','up','space'])
    time.sleep(0.2)
    pydirectinput.press('down',2,0.1)

    run(1.7)

    # 第一张图
    pydirectinput.press(['ctrl','a'])
    time.sleep(0.6)
    pydirectinput.press('down')
    run(0.94)
    listener()


    #第二张图
    run(0.88)
    pydirectinput.press('down')

    pydirectinput.press(['ctrl','s'])
    time.sleep(1.6)


    run(0.98)
    listener()


    #第三张图
    # print("第三张图")
    run(0.6)
    pydirectinput.press(['alt','s'])
    time.sleep(1.23)
    # pydirectinput.press('down')

    run(1.55)

    #第四张图
    # print("第四张图")
    run(0.7)
    pydirectinput.press(['ctrl','a'])
    time.sleep(1.6)
    pydirectinput.press('down')

    run(1.05)
    listener()
    #Boss
    run(random.uniform(0.5,0.88))
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

    pydirectinput.press('s')
    time.sleep(0.84)
    # pydirectinput.press(['right','space'])
    # time.sleep(0.5)

    pydirectinput.press('q')
    time.sleep(0.4)
    pydirectinput.press('alt')
    time.sleep(0.35)
    pydirectinput.press('r')

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

    run(1.79)
    pydirectinput.press('s')
    time.sleep(0.85)

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
    pydirectinput.press('down')

    run(1.04)
    listener()

    # 第二张图
    run(1.32)

    time.sleep(0.34)
    pydirectinput.press('down',3,0.08)
    pydirectinput.press('a')
    run(0.49)
    listener()


    #第三张图
    run(0.83)
    time.sleep(0.23)
    pydirectinput.press('a')
    time.sleep(0.41)

    run(1.3)
    listener()

    #第4张图
    run(0.63)
    pydirectinput.press('a')
    time.sleep(0.36)

    pydirectinput.press('down')

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

    autow(2.9)



def fengfa():
    # 上buff
    pydirectinput.press(['right', 'right', 'space'])
    time.sleep(0.58)
    # pydirectinput.press('down')
    # pydirectinput.press('g')

    run(1.43)

    # 第一张图
    pydirectinput.press('alt')

    run(2.318)
    pydirectinput.press('down')
    # 第二张图

    pydirectinput.press('s')
    time.sleep(1.2)
    pydirectinput.press('g')


    run(1.47)
    pydirectinput.press('ctrl')
    pydirectinput.press('g')

    # 第四张图
    run(1.68)
    pydirectinput.press('q')
    time.sleep(0.47)
    pydirectinput.press('g')
    pydirectinput.press('down')
    time.sleep(0.08)

    #Boss
    run(1.7)

    pydirectinput.press('g')
    pydirectinput.press('y')
    time.sleep(5)
    pydirectinput.press('r')
    time.sleep(1.22)
    autow(3)

