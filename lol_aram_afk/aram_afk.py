# ARAM 掛機

import pyautogui
import pydirectinput
import time

pyautogui.FAILSAFE = True
size = pyautogui.size()

welcome = (817, 139, 278, 34)
find_name1 = (700, 310, 60, 340)
find_name2 = (1270, 310, 60, 340)

blue_castle = (1576, 1002)
red_castle = (1847, 742)

hp = (681, 1029, 414, 17)

'''
camera = (1440, 1057)
hp_get_hurt = (1052, 1029, 43, 17)
hp_two_thirds = (956, 1029, 98, 17)
hp_one_thirds = (681, 1029, 139, 17)
'''

# 暫停 s 秒
def s(second):
    time.sleep(second)

# 點一下
def click(point):
    pyautogui.mouseDown(point)
    pyautogui.mouseUp(point)

# 點一下右鍵
def walk(point):
    pyautogui.mouseDown(point, button='right')
    pyautogui.mouseUp(point, button='right')

# 鼠標移動到位置 點T快捷指定攻擊
def attack(point):
    pyautogui.moveTo(point)
    pydirectinput.press('t')

# 沒找到圖回傳 None
def onscreen(src, box):
    return pyautogui.locateOnScreen('images/%s.png'%src, region=box, confidence=0.6)

# 重複每秒找一次圖直到找到
def until_find(src, box):
    while True:
        find = onscreen(src, box)
        if find != None:
            break
        time.sleep(1)

# ____________________________________________________________________________________________________

# 倒數幾秒之後開始
def prepare(second):
    for s in range(second, 0, -1):
        print(s)
        time.sleep(1)
    print('----------開始----------')

# 每秒搜尋一次 歡迎來到咆哮深淵! 直到找到
def wait_game_start():
    welcome = (817, 139, 278, 34)
    while True:
        welcome_blue = onscreen('welcome_blue', welcome)
        welcome_red = onscreen('welcome_red', welcome)
        if (welcome_blue != None) | (welcome_red != None):
            break
        time.sleep(1)

# 鎖定視角
def lock_view():
    pydirectinput.press('u')

# 確認紅藍方
def confirm_color():
    pydirectinput.press('o')

    find_name1 = (700, 310, 60, 340)
    find_name2 = (1270, 310, 60, 340)

    blue_castle = (1576, 1002)
    red_castle = (1847, 742)

    global enemy_castle
    global own_castle

    blue = onscreen('name', find_name1)
    red = onscreen('name', find_name2)
    if (blue != None) & (red == None):
        print('你在藍方')
        enemy_castle = red_castle
        own_castle = blue_castle
        # skills = (size.width/2 + 300, size.height/2 - 300)
    elif (blue == None) & (red != None):
        print('你在紅方')
        enemy_castle = blue_castle
        own_castle = red_castle
        # skills = (size.width/2 - 100, size.height/2 + 100)
    else:
        # 錯誤訊息
        print('無法判斷紅藍方 QAQ \n')
        print('藍 : ')
        print(blue)
        print('紅 : ')
        print(red)
    
    pydirectinput.press('o')
# ____________________________________________________________________________________________________


prepare(5)

print('等30秒再出去')
# wait_game_start()
print('30秒到了 gogo')

print('鎖定視角')
lock_view()

# confirm_color()

enemy_castle = blue_castle
own_castle = red_castle


# 正式開始
# 攻擊 -> 被打撤退 掛機30秒 -> 動一下 -> 再掛機30秒 -> 重複
while True:
    print('攻擊!!')
    attack(enemy_castle)
    while True:
        hp_img = pyautogui.screenshot(region=hp)
        time.sleep(0.5)
        hurt = pyautogui.locateOnScreen(hp_img, region=hp, confidence=0.8)
        if hurt == None:
            print('哭阿被打了 QAQ')
            break
    
    print('撤退 >w<')
    walk(own_castle)
    time.sleep(30)
    
    print('動一下XD')
    attack(enemy_castle)
    time.sleep(1)
    walk(own_castle)
    time.sleep(30)

'''
    
# pydirectinput.keyDown('ctrl')
# pydirectinput.press('q')
# pydirectinput.press('w')
# pydirectinput.press('e')
# pydirectinput.keyUp('ctrl')

while True:
    hp_img = pyautogui.screenshot(region=hp)
    time.sleep(1)
    # s(2)
    # walk(own_castle)
    # s(1)
    hurt = pyautogui.locateOnScreen(hp_img, region=hp, confidence=0.8)
    if hurt == None:
        print('哭阿被打了')
        walk(own_castle)
        pyautogui.moveTo(skills)
        pydirectinput.press('q')
        pydirectinput.press('w')
        pydirectinput.press('e')
        walk(own_castle)
        s(10)
    attack(enemy_castle)

'''