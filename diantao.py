import uiautomator2 as u2
import random
import time
from utils import hd


# d = u2.connect_usb("c635d924")  # id 为 adb devices 命令中得到的设备 id

# 无线连接

d = u2.connect("192.168.168.190:5566")  #
width, height = d.window_size()
print(d.info)
d.app_stop("com.taobao.live")
d.app_start("com.taobao.live")
d.sleep(3)

d(resourceId="com.taobao.live:id/gold_center_image").click()
d.sleep(3)
# d.app_stop_all()
# d.click(1090, 536)
# d.app_start("com.")
startTm = time.time()

while(True):
    if(d(text="今日签到").exists):
        break
    hd(d,1,3,startTm)
d(text="今日签到").click()
d.sleep(2)

while(len(d(text="去完成"))>0):
    d(text="去完成").click()
    d.sleep(1)
    runtime = time.time()
    if(d(text="奖励将于").exists or d(text="跳过").exists()):
        d.sleep(50)
        d(resourceId="android:id/button2").click_exists()
    else:
        while(time.time()-runtime<45):
            hd(d,4,7,startTm)
            d(resourceId="android:id/button2").click_exists()
    d.press("back")
    d(resourceId="com.byted.pangle.m:id/tt_reward_full_count_down_after").click_exists()
    d(resourceId="com.taobao.live:id/negative").click_exists()
    if(d(text="已领取奖励").exists):
        d(text="跳过").click()
    d(text="跳过").click_exists()
    d.sleep(0.5)
    d(resourceId="com.byted.pangle.m:id/tt_negtive").click_exists()
    d(text="坚持退出").click_exists()
    d.sleep(1)
    d(text="继续做任务").click_exists()




