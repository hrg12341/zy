import os

import uiautomator2 as u2
import random
import time
from utils import hd,TimePrint


# d = u2.connect_usb("c635d924")  # id 为 adb devices 命令中得到的设备 id
#
# 无线连接

d = u2.connect("192.168.168.190:5566")  #
# d = u2.connect("192.168.1.103:5566")  #
print(d.info)
width, height = d.window_size()
startTm = time.time()
os.system("python -m weditor")
# print(d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]').click())
# for elem in d.xpath('//android.widget.TextView').all():
#     print(elem)
#     print("Text:",elem.text)
# while(True):
    # hd(d,6,10,startTm)
    # width, height = d.window_size()
    # sx = random.randrange(650, 850) / 1000.0
    # ex = random.randrange(200, 300) / 1000.0
    # sy = random.randrange(450, 650) / 1000.0
    # ey = random.randrange(400, 650) / 1000.0
    # dur = random.randrange(67, 146) / 1000.0
    # d.swipe(sx * width, sy * height, ex * width, ey * height, duration=dur)
    # second = random.randrange(4, 7)
    # d.sleep(second)
    #
    # print("随机等待" + str(second) + "s")
    # TimePrint(startTm)