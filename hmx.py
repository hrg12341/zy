import uiautomator2 as u2
import random
import time

def TimePrint():
    now =time.time()
    t = int(now - startTm)
    if(t<60):
        print("已运行" + str(t) + "s")
    elif(t<3600):
        print("已运行" + str(t//60) + "m"+str(t%60)+"s")
    else:
        print("已运行" + str(t // 3600) + "h" + str((t % 3600)//60) + "m"+ str(t % 60) + "s")


d = u2.connect_usb("71bc638d")  # id 为 adb devices 命令中得到的设备 id

# 无线连接

d = u2.connect("192.168.1.105:5567")  #
width, height = d.window_size()
print(d)
d.sleep(3)
# d.app_stop_all()
# d.click(1090, 536)
# d.app_start("com.")
startTm = time.time()

while(True):
    sx = random.randrange(450,650)/1000.0
    ex = random.randrange(500,650)/1000.0
    sy = random.randrange(750,850)/1000.0
    ey = random.randrange(300,550)/1000.0
    dur = random.randrange(187,256)/1000.0
    d.swipe(sx*width,sy*height,ex*width,ey*height,duration=dur)
    second = random.randrange(5,16)
    d.sleep(second)

    print("随机等待"+str(second)+"s")
    TimePrint()




