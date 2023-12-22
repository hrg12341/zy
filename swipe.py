import uiautomator2 as u2
import random
import time
from utils import hd


# d = u2.connect_usb("c635d924")  # id 为 adb devices 命令中得到的设备 id

# 无线连接

d = u2.connect("192.168.168.190:5566")  #
width, height = d.window_size()
print(d)

d.sleep(3)


# d.app_stop_all()
# d.click(1090, 536)
# d.app_start("com.")
startTm = time.time()



while(len(d(text="去完成"))>0):
    d(text="去完成").click()
    d.sleep(1)
    runtime = time.time()
    if(d(text="奖励将于").exists):
        d.sleep(50)
        d(resourceId="android:id/button2").click_exists()
    else:
        while(time.time()-runtime<45):
            hd(d,4,7,startTm)
            d(resourceId="android:id/button2").click_exists()
    d.press("back")
    d(resourceId="com.byted.pangle.m:id/tt_reward_full_count_down_after").click_exists()
    if(d(text="已领取奖励").exists):
        d(text="跳过").click()
    d.sleep(1)
    d(text="继续做任务").click_exists()





