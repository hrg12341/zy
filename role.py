import time
from dnf import ms,huahua,axl,lvren,naima,nq,zhaohuan
import math
from pynput import keyboard
import threading
import tkinter as tk

app = tk.Tk()
count = math.ceil(188 / 6)
type = 1

def on_press(key):
    try:
        if key == keyboard.Key.f2:
            start()
        if key == keyboard.Key.f3:
            stop()
    except AttributeError:
        # 禁用 PyDirectInput 键盘监听
        pass

def start():
    global stop_event,t
    stop_event.clear()
    # 监听键盘事件
    t = threading.Thread(target=event, args=(stop_event,)).start()

def stop():
    global stop_event
    stop_event.set()
    t.join()
def choseRole():
    if(type==1):
        return nq(),"女枪"
    elif (type == 2):
        return naima(), "奶妈"
    elif (type == 3):
        return lvren(), "旅人"
    elif (type == 4):
        return ms(), "缪斯"
    elif (type == 5):
        return huahua(), "花花"
    elif (type == 7):
        return axl(), "阿修罗"
    elif (type == 8):
        return zhaohuan(),"召唤"


# if __name__ == "__main__":
def event(stop_event):
    role,name = choseRole(type)
    # wait 2s
    while not stop_event.is_set():
        print(name + "开始刷图")
        time.sleep(2)
        for i in range(count):
            print(name+"第"+str(i+1)+"次刷图")
            role



def choseRole(type):
    if(type==1):
        return nq(),"女枪"
    elif (type == 2):
        return naima(), "奶妈"
    elif (type == 3):
        return lvren(), "旅人"
    elif (type == 4):
        return ms(), "缪斯"
    elif (type == 5):
        return huahua(), "花花"
    elif (type == 7):
        return axl(), "阿修罗"
    elif(type==8):
        return zhaohuan(),"召唤"



keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()


stop_event = threading.Event()
app.title("刷深渊图")
app.geometry("600x150")
app.mainloop()