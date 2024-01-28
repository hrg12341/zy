import os
import time
# import cv2
# import pyautogui
# from skimage.metrics import structural_similarity as ssim

# 1.女枪
# 2.奶妈
# 3.旅人
# 4.缪斯
# 5.花花
# 6.风法
# 7.阿修罗
# 8.召唤

type = 7
pl = 98
tu = 1

def shenyuan():
    os.system("python shenyuan.py " + str(pl) + " " + str(type))

def fengbao():
    os.system("python fengbao.py " + str(pl) + " " + str(type))

if __name__=="__main__":
    if(tu == 1):
        shenyuan()
    else:
        fengbao()
