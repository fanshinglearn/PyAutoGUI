# 阿福快打自動送頭

import pyautogui
import time



# 我的隊伍
team = 'blue'
# team = 'red'



# 座標
if team == 'blue':
    fort_pos = (30,750)
    mid_pos = (1540,1050)
    home_pos = (1540,1050)
else:
    fort_pos = (1700,420)
    mid_pos = (1889,694)
    home_pos = (1889,694)

pyautogui.FAILSAFE = True
time.sleep(5)

while True:
    time.sleep(1)
    die = pyautogui.locateOnScreen('die.png',region=(1438,553,1515,624))
    if die == None:
        print('活著')
        
        #砲台
        print('砲台')
        pyautogui.moveTo(fort_pos)
        pyautogui.mouseDown(button="right")
        pyautogui.mouseUp(button="right")

        time.sleep(2)

        #中飛
        print('中飛')
        pyautogui.moveTo(mid_pos)
        pyautogui.mouseDown()
        pyautogui.mouseUp()

        time.sleep(3)

        #判斷死了沒
        while die == None:
            #溫泉
            print('溫泉')
            pyautogui.moveTo(home_pos)
            pyautogui.mouseDown(button="right")
            pyautogui.mouseUp(button="right")
            time.sleep(3)
            die = pyautogui.locateOnScreen('die.png',region=(1438,553,1515,624))
        
    else:
        print('死了')
