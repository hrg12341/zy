import uiautomator2 as u2
import random
import time
from utils import hd,hd_zfb
startTm = time.time()
# d = u2.connect()
# d = u2.connect("192.168.168.190:5566")
# d = u2.connect("192.168.168.167:5568")
d = u2.connect("192.168.1.101:5566")  #
print(d.info)
# d.app_stop("com.eg.android.AlipayGphone")
# d.app_start("com.eg.android.AlipayGphone")
# d.sleep(2)
width, height = d.window_size()
# d(resourceId="com.alipay.android.tablauncher:id/tab_description", text="生活").click()
# d(resourceId="com.alipay.android.tablauncher:id/tab_description", text="视频").click()
# d.click(0.5*width,0.90*height)

d(resourceId="com.alipay.android.living.dynamic:id/bgImageView").click_exists(timeout=1)
d(text="立即签到领").click_exists(timeout=2)
hd(d,3,7,startTm)
# d.xpath('//*[@resource-id="com.alipay.android.living.dynamic:id/tab_layout"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]').click()
while(True):
    hd_zfb(d,8,18,startTm)
    time.sleep(3)
    if(d(resourceId="com.alipay.android.living.dynamic:id/image").exists() == False):
        hd(d,1,2,startTm)

    now = time.time()
    if(now-startTm>320000):break