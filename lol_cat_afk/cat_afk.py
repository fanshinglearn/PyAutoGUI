import pyautogui
import pydirectinput
import time

pyautogui.FAILSAFE = True

# 貓咪技能加點順序
# cat_skill = ['','e','q','e','w','e','r','e','w','e','w','r','w','q','q','q','r','q','q']

# 隊友1~4附身座標
tm1 = 1578,595
tm2 = 1676,595
tm3 = 1773,595
tm4 = 1868,595

# 選擇隊友
# tm = input('選擇隊友 (1~4 從左到右): ')
tm = 0
if tm == '1':
    tm = tm1
elif tm == '2':
    tm = tm2
elif tm == '3':
    tm = tm3
else:
    tm = tm4

# 切畫面
time.sleep(3)

# 鎖定視角
pydirectinput.press('u')

# 升級E技能
pydirectinput.keyDown('ctrl')
pydirectinput.press('e')
pydirectinput.keyUp('ctrl')

# 買初始裝備
pydirectinput.press('p')
pydirectinput.click(1061, 122)
pydirectinput.rightClick()

# __________________________________________________________________________________________

# while True:
#     pyautogui.moveTo(tm)
#     pydirectinput.press('w')

# while True:
#     die = pyautogui.locateOnScreen('cat_die.png',region=(1437,557,80,62))
#     if die == None:
#         print('活著')

#         # 升級技能
#         new_skill = pyautogui.locateOnScreen('new_skill.png',region=(730,894,920,947))    
#         if new_skill != None:
#             print('升級技能')
#             pydirectinput.keyDown('ctrl')
#             pydirectinput.press('r')
#             pydirectinput.press('e')
#             pydirectinput.press('w')
#             pydirectinput.press('q')
#             pydirectinput.keyUp('ctrl')

#         # 附身隊友
#         car = pyautogui.locateOnScreen('cat_on.png',region=(792,944,858,1011))
#         if car == None:
#             print('附身隊友')
#             pyautogui.moveTo(tm)
#             pydirectinput.press('w')
#             pydirectinput.press('e')
#             time.sleep(3)
#             car = pyautogui.locateOnScreen('cat_on.png',region=(792,944,858,1011))
#         else:
#             pydirectinput.press('e')
#     else:
#         print('死了')
