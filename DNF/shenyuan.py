import time
from skill import *
import math
import sys
import pydirectinput

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
        if(i!=count-1):
            pydirectinput.press('f10')
            time.sleep(2.9)



def choseRole(type):
    role = ["女枪", "奶妈", "旅人", "缪斯", "花花",
            "风法", "阿修罗", "召唤", "帕拉丁","女弹药"]
    return role[type-1]

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
    elif (type == 9):
        pld()
    elif (type == 10):
        ndy()

if __name__ == "__main__":
    global count,type
    pl = int(sys.argv[1])
    type = int(sys.argv[2])
    print(pl)
    count = math.ceil(pl / 8)
    main()