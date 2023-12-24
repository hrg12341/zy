import uiautomator2 as u2
import random
import time
from utils import hd,TimePrint

d = u2.connect("192.168.1.104:5566")
print(d.info)
startTm = time.time()

while(True):
    # hd(d,40,60,startTm)
    width, height = d.window_size()
    sx = random.randrange(750, 900) / 1000.0
    sy = random.randrange(450, 650) / 1000.0
    d.click(sx,sy)
    second = random.randrange(4, 7)
    d.sleep(second)
    print("随机等待" + str(second) + "s")
    TimePrint(startTm)