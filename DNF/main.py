import os
import time
import cv2
import pyautogui
from skimage.metrics import structural_similarity as ssim

# 1.女枪
# 2.奶妈
# 3.旅人
# 4.缪斯
# 5.花花
# 6.风法
# 7.阿修罗
# 8.召唤
# 9.帕拉t丁

type = 1
pl = 1
tu = 2

def shenyuan():
    os.system("python shenyuan.py " + str(pl) + " " + str(type))

def fengbao():
    os.system("python fengbao.py " + str(pl) + " " + str(type))

if __name__=="__main__":
    if(tu == 1):
        shenyuan()
    else:
        fengbao()
    # image1 = cv2.cvtColor(cv2.imread("png/loc.png"), cv2.COLOR_BGR2GRAY)
    # image2 = cv2.cvtColor(cv2.imread("png/compare.png"), cv2.COLOR_BGR2GRAY)
    #
    # ssim_value = ssim(image1, image2)
    # print(ssim_value)