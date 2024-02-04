# This is a sample Python script.
import time
import numpy as np
import pyautogui
import pytesseract
from PIL import Image
import easyocr
# from skimage.metrics import structural_similarity as ssim

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def window_capture(filename):
#     hwnd = win32gui.FindWindow(None, "地下城与勇士: 创新世纪")
#     # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
#     hwndDC = win32gui.GetWindowDC(hwnd)
#     win32gui.SetForegroundWindow(hwnd)
#     # 根据窗口的DC获取mfcDC
#     mfcDC = win32ui.CreateDCFromHandle(hwndDC)
#     # mfcDC创建可兼容的DC
#     saveDC = mfcDC.CreateCompatibleDC()
#     # 创建bigmap准备保存图片
#     saveBitMap = win32ui.CreateBitmap()
#     # 获取监控器信息
#     left, top, right, bottom = win32gui.GetWindowRect(hwnd)
#     width = right - left
#     height = bottom - top
#     # MoniterDev = win32api.EnumDisplayMonitors(None, None)
#     # w = MoniterDev[0][2][2]
#     # h = MoniterDev[0][2][3]
#     # print w,h　　　#图片大小
#     # 为bitmap开辟空间
#     saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
#     # 高度saveDC，将截图保存到saveBitmap中
#     saveDC.SelectObject(saveBitMap)
#     # 截取从左上角（0，0）长宽为（w，h）的图片
#     saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)
#     saveBitMap.SaveBitmapFile(saveDC, filename)
#     return width, height


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # # screenshot = pyautogui.screenshot("loc.png")
    # time.sleep(2)
    # screenshot = pyautogui.screenshot(region=(1480,305,295,35))
    # screenshot.save("screenshot.png")
    #
    #
    # image1 = Image.open("DNF/png/loc.png").convert("L")
    # image2 = Image.open("screenshot.png").convert("L")
    #
    # mse = np.square((np.array(image2)-np.array(image1)).mean())
    #
    # print(mse)
    reader = easyocr.Reader(['ch_sim'])
    now = time.time()

    # result = reader.readtext("DNF/png/loc.png",detail=0)
    result = reader.readtext("screenshot.png",detail=0)
    print(result)
    print("取的物"in (str)(result))
    print(time.time()-now)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
