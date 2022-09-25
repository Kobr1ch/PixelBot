from vision import Vision
from ruler import *
import win32gui
import keyboard
import os
import time
from windowcapture import *
import cv2 as cv
import numpy as np

from subprocess import Popen, PIPE

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#настроить прослушивание процесса
# while True:
#     prs = Popen('tasklist', stdout=PIPE).stdout.readlines()
#     pr_list = [prs[i].decode('cp866', 'ignore').split()[0] for i in range(3, len(prs))]
#     if 'l2.bin' in pr_list:
#         break
#     else:
#         relogin()

# initialize the WindowCapture class
go_to_sleep(10, 10)
with open("hero_name.txt") as file:
    win_name = file.read()

try:
    win_cap = WindowCapture(win_name)
    hwnd = win32gui.FindWindow(None, win_name)
    win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
    win32gui.SetForegroundWindow(hwnd)
except:
    print('ошибка окна 1')


#добавить проверку на рестарт
# click_image_true(win_cap, 1153, 652 + 20)
# go_to_sleep(5, 11)
# click_image_true(win_cap, 888 - random.randint(0, 3) * 40, 596)
# go_to_sleep(5, 7)
# click_image_true(win_cap, 983, 635)

# initialize the Vision classwin32api.keybd_event(0x11, 0, 0, 0)

vision_point = Vision('v gorod_bottom_2.png') #табличка смерти+ встать за л монеты
vision_point_2 = Vision('bez_strafa.png') #табличка смерти + принятие в город
vision_point_3 = Vision('test_2.bmp') #автобой
vision_point_4 = Vision('disconect.png') #дисконект
vision_point_5 = Vision('mir_zona.bmp') #мирная зона
vision_point_5_1 = Vision('mir_zina_gray.bmp') #мирная зона 2
#vision_point_5_2 = Vision('mir_red.bmp') #pvp зона
vision_point_6 = Vision('nagrada_zaLogin.bmp') #награда за логин
loop_time = time.time()


while(True):
    #print(win32gui.GetWindowRect(wincap.hwnd))
    # get an updated image of the game
    win_cap = WindowCapture(win_name)
    try:
        win_cap = WindowCapture(win_name)
        hwnd = win32gui.FindWindow(None, win_name)
        win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
        win32gui.SetForegroundWindow(hwnd)
    except:
        print('ошибка окна в цикле')

    #click_image_rc(win_cap, 584, 309-20)
    go_to_sleep(2, 2)
    screenshot = win_cap.get_screenshot()


    # display the processed image ('rectangles' тест окно)
    #points_3 = vision_point_3.find(screenshot[278:432, 538:732], 0.5)  # проверка дисконекта
    points = vision_point.find(screenshot[278:312, 538:732], 0.5) #табличка смерти + принятие в город
    points_2 = vision_point_2.find(screenshot[278:412, 538:732], 0.5)
    points_3 = vision_point_3.find(screenshot[516:756, 829:1113], 0.5) # проверка автобоя
    points_4 = vision_point_4.find(screenshot[378:432, 582:698], 0.5) # проверка дисконекта
    points_5 = vision_point_5.find(screenshot[3:100, 1080:1280], 0.5)  # мирная зона
    points_5_1 = vision_point_5_1.find(screenshot[3:100, 1080:1280], 0.5)  # мирная зона
    #points_5_2 = vision_point_5_2.find(screenshot[3:40, 1033:1115], 0.5, 'rectangles')  # мирная зона
    points_6 = vision_point_6.find(screenshot[3:100, 850:1100], 0.5)  # награда за релогин

    print(points_5_1)

    if len(points) > 0 and len(points_2) == 0:

        try:
            win_cap = WindowCapture(win_name)
            hwnd = win32gui.FindWindow(None, win_name)
            win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
            win32gui.SetForegroundWindow(hwnd)
        except:
            print('ошибка окна на ресе')

        click_image_true(win_cap, 642, 373 + 30)
        go_to_sleep(1, 5)
        click_image_true(win_cap, 590, 447+20)
        go_to_sleep(11, 30)
        click_image_true(win_cap, 888 - random.randint(0, 3) * 40, 596)
        go_to_sleep(10, 15)
        click_image_true(win_cap, 983, 635)
        go_to_sleep(1, 1)
    if len(points_2) > 0:
        try:
            win_cap = WindowCapture(win_name)
            hwnd = win32gui.FindWindow(None, win_name)
            win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
            win32gui.SetForegroundWindow(hwnd)
        except:
            print('ошибка окна на бесплатном ресе')

        click_image_true(win_cap, 641, 389+20)
        go_to_sleep(1, 3)
        click_image_true(win_cap, 623, 410 + 20)
        go_to_sleep(1, 3)
        click_image_true(win_cap, 627, 425 + 20)
        go_to_sleep(1, 3)
        click_image_true(win_cap, 888 - random.randint(0, 3) * 40, 596)
        go_to_sleep(10, 15)
        click_image_true(win_cap, 983, 635)
        go_to_sleep(1, 1)
    if len(points_3) == 0 and len(points_4) == 0: #автобой
        try:
            win_cap = WindowCapture(win_name)
            hwnd = win32gui.FindWindow(None, win_name)
            win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
            win32gui.SetForegroundWindow(hwnd)
        except:
            pass
        go_to_sleep(1, 3)
        click_image_true(win_cap, 983, 635)
        #click_image_true(win_cap, 543, 515+20) #проверка скила
        go_to_sleep(1, 3)
        continue
    if len(points_4) > 0: #дисконект
        try:
            win_cap = WindowCapture(win_name)
            hwnd = win32gui.FindWindow(None, win_name)
            win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
            win32gui.SetForegroundWindow(hwnd)
        except:
            pass
        click_image_true(win_cap, 640, 408 + 20)
        go_to_sleep(5, 5)
        relogin()
        go_to_sleep(15, 20)
        with open("hero_name.txt") as file:
            win_name = file.read()
        win_cap = WindowCapture(win_name)
        click_image_true(win_cap, 983, 635)
    if len(points_5) > 0 and len(points_5_1) >= 0: #проверка на город и боевую зону искл аден и грей
        try:
            win_cap = WindowCapture(win_name)
            hwnd = win32gui.FindWindow(None, win_name)
            win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
            win32gui.SetForegroundWindow(hwnd)
        except:
            pass
        go_to_sleep(5, 7)
        click_image_true(win_cap, 888 - random.randint(0, 3) * 40, 596)
        go_to_sleep(10, 15)
    if len(points_5) > 0 or len(points_5_1) == 0: #проверка на город и боевую зону
        try:
            win_cap = WindowCapture(win_name)
            hwnd = win32gui.FindWindow(None, win_name)
            win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
            win32gui.SetForegroundWindow(hwnd)
        except:
            pass
        go_to_sleep(5, 7)
        click_image_true(win_cap, 888 - random.randint(0, 3) * 40, 596)
        go_to_sleep(10, 15)
    loop_time = time.time()
    if len(points_6) > 0:
        click_image_true(win_cap, 1149, 651 + 20)
        go_to_sleep(2, 2)

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    # if cv.waitKey(1) == ord('q'):
    #     cv.destroyAllWindows()
    if keyboard.is_pressed('q'):
        break


print('Done.')