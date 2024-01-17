import time
from dnf import ms,huahua,axl,lvren,naima,nq,zhaohuan
import math
from pynput import keyboard
import threading
import tkinter as tk

pl = 140
type = 3

count = math.ceil(pl / 6)

def main():
    event()


def event():
    name = choseRole(type)
    # wait 2s
    print(name + "开始刷图")
    time.sleep(2)
    for i in range(count):
        print(name+"第"+str(i+1)+"次刷图")
        shuatu(type)



def  choseRole(type):
    if(type==1):
         return "女枪"
    elif (type == 2):
        return "奶妈"
    elif (type == 3):
        return  "旅人"
    elif (type == 4):
        return  "缪斯"
    elif (type == 5):
        return  "花花"
    elif (type == 7):
        return  "阿修罗"
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
    elif (type == 7):
        axl()
    elif (type == 8):
       zhaohuan()

if __name__ == "__main__":
    main()