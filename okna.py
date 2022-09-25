import ctypes, time
from vision import Vision
from ruler import *
import win32gui
import keyboard
import os
import pydirectinput
import ctypes, time
from windowcapture import *
import pyKey

# Bunch of stuff so that the script can send keystrokes to game #
os.chdir(os.path.dirname(os.path.abspath(__file__)))




with open("hero_name.txt") as file:
    win_name = file.read()
win_cap = WindowCapture(win_name)
hwnd = win32gui.FindWindow(None, win_name)
win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
win32gui.SetForegroundWindow(hwnd)

#pyKey.showKeys()

pyKey.pressKey('x')
