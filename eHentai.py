# 方便快速瀏覽網頁

import keyboard
import pydirectinput
import pyautogui
import time

next_page_pos = (1050, 979)

empty_area_pos1 = (1557 + 1903) / 2
empty_area_pos2 = (1032 + 120) / 2
empty_area_pos = (empty_area_pos1, empty_area_pos2)

translate_pos1 = (1423 + 1729) / 2
translate_pos2 = (393 + 420) / 2
translate_pos = (translate_pos1, translate_pos2)

# 下一頁
def next_page():
    last_pos = pyautogui.position()
    pyautogui.moveTo(next_page_pos)
    pyautogui.click()
    pyautogui.moveTo(last_pos)

# 回到上一頁
def previous_page():
    pyautogui.keyDown('alt')
    pyautogui.press('left')
    pyautogui.keyUp('alt')

# 關閉分頁
def close_page():
    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')

# chrome 切換下一個分頁
def ctrl_pagedown():
    pyautogui.keyDown('ctrl')
    pyautogui.press('pagedown')
    pyautogui.keyUp('ctrl')

# chrome 切換上一個分頁
def ctrl_pageup():
    pyautogui.keyDown('ctrl')
    pyautogui.press('pageup')
    pyautogui.keyUp('ctrl')

# 翻譯網頁
def translate():
    pyautogui.moveTo(empty_area_pos)
    pyautogui.mouseDown(button='right')
    pyautogui.mouseUp(button='right')
    pyautogui.moveTo(translate_pos)
    pyautogui.click()

# 縮小視窗
def reduce_window():
    pyautogui.keyDown('alt')
    pyautogui.keyDown('space')
    pyautogui.press('n')
    pyautogui.keyUp('space')
    pyautogui.keyUp('alt')

print('已啟動')
while True:
    # 下一頁
    if keyboard.is_pressed('0'):
        next_page()
    
    # chrome 切換上一個分頁
    if keyboard.is_pressed('left'):
        ctrl_pageup()
    
    # chrome 切換下一個分頁
    if keyboard.is_pressed('right'):
        ctrl_pagedown()
    
    # 回到上一頁
    if keyboard.is_pressed('up'):
        previous_page()
    
    # 關閉分頁
    if keyboard.is_pressed('delete'):
        close_page()
    
    # 翻譯網頁
    if keyboard.is_pressed('t'):
        translate()
    
    # 翻譯網頁
    if keyboard.is_pressed('esc'):
        reduce_window()
    
    time.sleep(0.1)
