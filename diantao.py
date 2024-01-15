import uiautomator2 as u2
import random
import time
from utils import hd

# d(resourceId="android:id/button2").click()').click()  拒绝
# d = u2.connect_usb("c635d924")  # id 为 adb devices 命令中得到的设备 id

# 无线连接
# 192.168.168.190:5566
d = u2.connect("192.168.168.190:5566")  #
# d = u2.connect("192.168.1.105:5567")  #
width, height = d.window_size()
print(d.info)
d.app_stop("com.taobao.live")
d.app_start("com.taobao.live")
d.sleep(3)

d(resourceId="com.taobao.live:id/gold_center_image").click_exists()
d(resourceId="com.taobao.live:id/gold_egg_image").click_exists()
d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]').click_exists()
d.sleep(3)
# d.app_stop_all()
# d.click(1090, 536)
# d.app_start("com.")
startTm = time.time()


def jrqd():
    while (True):
        if (d(text="今日签到").exists):
            break
        hd(d, 1, 3, startTm)
    d(text="今日签到").click()
    d.sleep(2)
    if (d.xpath('//*[@resource-id="J_dialogContainer"]/android.view.View[1]').exists):
        d(text="O1CN01qE4nNy1M45HMjL7jz_!!6000000001380-2-tps-60-60.png_").click_exists()
        d(text="我知道了").click_exists()
        d.sleep(1)
    while (len(d(text="去完成")) > 0):
        d(text="去完成").click()
        d.sleep(1)
        runtime = time.time()
        if (d(text="奖励将于").exists or d(text="跳过").exists() or d(text="| 跳过").exists()):
            d.sleep(50)
            d(resourceId="android:id/button2").click_exists()
            d.xpath(
                '//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.ImageView[1]').click_exists()
        else:
            while (time.time() - runtime < 45):
                hd(d, 4, 7, startTm)
                d(resourceId="android:id/button2").click_exists()
        d.press("back")
        d(resourceId="com.byted.pangle.m:id/tt_reward_full_count_down_after").click_exists()
        d.xpath(
            '//android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click_exists()
        d(resourceId="com.taobao.live:id/negative").click_exists()
        if (d(text="已领取奖励").exists):
            d(text="跳过").click()
        d(text="跳过").click_exists()
        d(text="| 跳过").click_exists()
        d(text="|跳过").click_exists()
        d.sleep(0.5)
        d(resourceId="com.byted.pangle.m:id/tt_negtive").click_exists()
        d(text="坚持退出").click_exists()
        d(text="残忍离开").click_exists()
        d.sleep(1)
        d(text="继续做任务").click_exists()

jrqd()


def zqk():
    # 赚钱卡
    d.app_stop("com.taobao.live")
    d.app_start("com.taobao.live")
    d.sleep(3)

    d(resourceId="com.taobao.live:id/gold_center_image").click_exists()
    d(resourceId="com.taobao.live:id/gold_egg_image").click_exists()
    d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]').click_exists()
    d.sleep(1)
    while (True):
        if (d(text="赚钱卡").exists):
            break
        hd(d, 1, 3, startTm)
    d(text="赚钱卡").click()
    d.sleep(1)
    d(text="O1CN01Rf0rA61RoPZl3OjLt_!!6000000002158-2-tps-54-54.png_Q75.jpg_").click()

    while (len(d(text="去完成")) > 1):
        d(text="去完成").click()
        d.sleep(1)
        runtime = time.time()
        if (d(text="奖励将于").exists or d(text="跳过").exists() or d(text="| 跳过").exists()):
            d.sleep(50)
            d(resourceId="android:id/button2").click_exists()
            d.xpath(
                '//*[@resource-id="android:id/content"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.ImageView[1]').click_exists()
        else:
            while (time.time() - runtime < 45):
                hd(d, 4, 7, startTm)
                d(resourceId="android:id/button2").click_exists()
        d.press("back")
        d(resourceId="com.byted.pangle.m:id/tt_reward_full_count_down_after").click_exists()
        d.xpath(
            '//android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click_exists()
        d(resourceId="com.taobao.live:id/negative").click_exists()
        if (d(text="已领取奖励").exists):
            d(text="跳过").click()
        d(text="跳过").click_exists()
        d(text="| 跳过").click_exists()
        d(text="|跳过").click_exists()
        d.sleep(0.5)
        d(resourceId="com.byted.pangle.m:id/tt_negtive").click_exists()
        d(text="坚持退出").click_exists()
        d(text="残忍离开").click_exists()
        d.sleep(1)
        d(text="继续做任务").click_exists()


# zqk()












