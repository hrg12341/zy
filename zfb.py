import uiautomator2 as u2
import random
import time
from utils import hd

d = u2.connect("192.168.168.190:5566")
print(d.info)
d.app_start("com.eg.android.AlipayGphone")
d.sleep(2)
d(resourceId="com.alipay.android.tablauncher:id/tab_description", text="生活").click()
startTm = time.time()
# d.xpath('//*[@resource-id="com.alipay.android.living.dynamic:id/tab_layout"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]').click()
while(True):
    hd(d,5,8,startTm)
    if(d(resourceId="com.alipay.android.living.dynamic:id/redPacketIv").exists() == False):
        d.press("back")
    now = time.time()
    if(now-startTm>1200):break