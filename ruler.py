import pydirectinput
from windowcapture import WindowCapture
import win32gui, win32api, win32con
import time
import random
import os
from subprocess import Popen, PIPE


def click_image(wincap, x, y): # подтягивает координаты из поиска
    coord = win32gui.GetWindowRect(wincap.hwnd)
    pydirectinput.moveTo(x + coord[0], y + coord[1]) #points_2[0] points_2[1]
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0) #работает
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0) #работает
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)  # работает
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def click_image_true(wincap, x, y): # кликает с указанием координат
    coord = win32gui.GetWindowRect(wincap.hwnd)
    pydirectinput.moveTo(x + coord[0], y + coord[1]) #points_2[0] points_2[1]
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0) #работает
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0) #работает
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)  # работает
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def click_image_rc(wincap, x, y): # кликает с указанием координат
    coord = win32gui.GetWindowRect(wincap.hwnd)
    pydirectinput.moveTo(x + coord[0], y + coord[1]) #points_2[0] points_2[1]
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN , 0, 0) #работает
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0) #работает
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)  # работает
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)  # работает

def go_to_sleep(x, y): # задержка, от и до в секундах
    z = random.randint(x, y)
    time.sleep(z)

def relogin():
    print('выполняю релогин')
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    while True:
        prs = Popen('tasklist', stdout=PIPE).stdout.readlines()
        pr_list = [prs[i].decode('cp866', 'ignore').split()[0] for i in range(3, len(prs))]
        if 'l2.bin' in pr_list:
            break
        else:
            with open("l2dir.txt") as file:
                dir_l2 = file.read()
            os.chdir(dir_l2)
            os.system('start AutologinN.bat')
            go_to_sleep(13, 13)

            try:
                win_cap = WindowCapture('MW-Essence')
                hwnd = win32gui.FindWindow(None, 'MW-Essence')
                win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
                win32gui.SetForegroundWindow(hwnd)
            except:
                continue
            click_image_true(win_cap, 588, 588 + 20)
            go_to_sleep(2, 2)
            click_image_true(win_cap, 572, 532 + 20)
            go_to_sleep(7, 10)
            click_image_true(win_cap, 642, 704 + 20)
            go_to_sleep(10, 15)
            click_image_true(win_cap, 1149, 651 + 20)
            go_to_sleep(15, 20)


# def window_finder(window_name):
#     while True:
#         hwnd = win32gui.FindWindow(None, window_name)
#         win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
#         win32gui.SetForegroundWindow(hwnd)
#         if win32gui.SetForegroundWindow(hwnd) == window_name:
#             return False

def start():
    exec(open("main.py").read())
