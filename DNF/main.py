import os

# 1.女枪
# 2.奶妈
# 3.旅人
# 4.缪斯
# 5.花花
# 6.风法
# 7.阿修罗
# 8.召唤

type = 6
pl = 19

def shenyuan():
    os.system("python shenyuan.py " + str(pl) + " " + str(type))

def fengbao():
    os.system("python fengbao.py " + str(pl) + " " + str(type))

shenyuan()
# fengbao()
