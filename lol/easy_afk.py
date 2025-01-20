# 在上下路二塔草叢來回走動掛機 (因為很容易被打穿到兵營 隊友又不投降時容易送太多被鎖帳)

import pyautogui
import time

# 1723,1044下草
# 1540,853上草

time.sleep(5)
pyautogui.moveTo(1723,1044)
pyautogui.mouseDown(button="right")
pyautogui.mouseUp(button="right")
time.sleep(30)
pyautogui.moveTo(1540,853)
pyautogui.mouseDown(button="right")
pyautogui.mouseUp(button="right")
time.sleep(1)
pyautogui.moveTo(1723,1044)
pyautogui.mouseDown(button="right")
pyautogui.mouseUp(button="right")
time.sleep(1)
pyautogui.moveTo(1540,853)
pyautogui.mouseDown(button="right")
pyautogui.mouseUp(button="right")

