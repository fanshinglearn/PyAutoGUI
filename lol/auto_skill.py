# 自動升級技能 (沒啥用)

import pyautogui
import pydirectinput
import time

lv3 = input('前三等升級技能順序 : ')
lv18 = input('主?副? : ') 

# 1到18等升級順序
skill = ['']
skill.append(lv3[0])
skill.append(lv3[1])
skill.append(lv3[2])
if lv3[0] == lv3[2]:
    if 'q' not in lv3:
        skill.append('q')
    if 'w' not in lv3:
        skill.append('w')
    if 'e' not in lv3:
        skill.append('e')
else:
    skill.append(lv18[0])
skill.append(lv18[0])
skill.append('r')
skill.append(lv18[0])
skill.append(lv18[1])
skill.append(lv18[0])
skill.append(lv18[1])
skill.append('r')
skill.append(lv18[1])
skill.append(lv18[1])
skill.append(lv18[2])
skill.append(lv18[2])
skill.append('r')
skill.append(lv18[2])
skill.append(lv18[2])

# skill = ['','e','q','e','w','e','r','e','w','e','w','r','w','q','q','q','r','q','q']
time.sleep(5)

for lv in range(1,19):
    new_skill = None
    while new_skill == None:
        time.sleep(1)
        new_skill = pyautogui.locateOnScreen('new_skill.png',region=(730,894,920,947), confidence=0.8)
    pydirectinput.keyDown('ctrl')
    pydirectinput.press(skill[lv])
    pydirectinput.keyUp('ctrl')
    print('現在%d等'%lv)
    time.sleep(5)