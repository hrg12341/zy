import random
import time

def TimePrint(startTm):
    now =time.time()
    t = int(now - startTm)
    if(t<60):
        print("已运行" + str(t) + "s")
    elif(t<3600):
        print("已运行" + str(t//60) + "m"+str(t%60)+"s")
    else:
        print("已运行" + str(t // 3600) + "h" + str((t % 3600)//60) + "m"+ str(t % 60) + "s")


def hd(d,start,end,startTm):
    width, height = d.window_size()
    sx = random.randrange(450,650)/1000.0
    ex = random.randrange(500,650)/1000.0
    sy = random.randrange(750,850)/1000.0
    ey = random.randrange(300,550)/1000.0
    dur = random.randrange(187,256)/1000.0
    d.swipe(sx*width,sy*height,ex*width,ey*height,duration=dur)
    second = random.randrange(start,end)
    d.sleep(second)

    print("随机等待"+str(second)+"s")
    TimePrint(startTm)

def hd_zfb(d,start,end,startTm):
    width, height = d.window_size()
    second = random.randrange(start,end)
    d.sleep(second)
    print("随机等待"+str(second)+"s")
    TimePrint(startTm)
    sx = random.randrange(450,650)/1000.0
    ex = random.randrange(500,650)/1000.0
    sy = random.randrange(750,850)/1000.0
    ey = random.randrange(300,550)/1000.0
    dur = random.randrange(187,256)/1000.0
    d.swipe(sx*width,sy*height,ex*width,ey*height,duration=dur)


