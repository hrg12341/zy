import time
from skill_fengbao import *
import math
import sys
import pydirectinput
import threading
import pyautogui
from skimage.metrics import structural_similarity as ssim
import cv2


def event():
    name = choseRole(type)
    # wait 2s
    print(name + "开始刷图")
    time.sleep(2)
    for i in range(count):
        print(name+"第"+str(i+1)+"次刷图_风暴")
        shuatu(type)
        if(i!=count-1):
            pydirectinput.press('f10')
            time.sleep(4.3)





def  choseRole(type):
    if(type==1):
         return "女枪"
    elif (type == 2):
        return "奶妈"
    elif (type == 3):
        return "旅人"
    elif (type == 4):
        return "缪斯"
    elif (type == 5):
        return "花花"
    elif (type == 6):
        return "风法"
    elif (type == 7):
        return "阿修罗"
    elif(type==8):
        return "召唤"

def shuatu(type):
    if (type == 1):
       nq()
    elif (type == 2):
        naima()
    elif (type == 3):
        lvren()
    elif (type == 4):
        ms()
    elif (type == 5):
        huahua()
    elif (type == 6):
        fengfa()
    elif (type == 7):
        axl()
    elif (type == 8):
       zhaohuan()

def run(t):
    pydirectinput.press('right')
        # time.sleep(0.1)
    pydirectinput.keyDown('right')
    time.sleep(t)
    pydirectinput.keyUp('right')

if __name__ == "__main__":
    global count,type

    pl = int(sys.argv[1])
    type = int(sys.argv[2])
    print(pl)
    count = math.ceil(pl / 6)
    event()
    # run()



