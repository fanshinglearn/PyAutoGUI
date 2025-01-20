import pyautogui
import time

pyautogui.FAILSAFE = True

pyautogui.PAUSE = 1

# 自走銅鑼座標
find = [1498, 481]

# 夜神模擬器左上右下座標
point1 = (find[0] - 207, find[1] - 440)
point2 = (find[0] + 354, find[1] + 545)
box = point1 + point2
center = ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

# 公會座標
guild = (point1[0] + 85, point1[1] + 650)

# 任務座標
mission = (point1[0] + 485, point1[1] + 675)
complete = (point1[0] + 445, point1[1] + 700)
enter = (point1[0] + 175, point1[1] + 610)


def find_picture(img):
    picture = None
    while picture == None:
        picture = pyautogui.locateOnScreen('%s.png'%img, region=box, confidence=0.7)
    return pyautogui.center(picture)

def has_picture(img):
    return(pyautogui.locateOnScreen('%s.png'%img, region=box, confidence=0.7))

# 主程式
print('公會')
pyautogui.click(guild)
print('任務')
pyautogui.click(mission)

if has_picture('complete') != None:
    print('完成任務')
    pyautogui.click(complete)
    pyautogui.click(enter)
    time.sleep(1)
    pyautogui.click(center)


# elif has_picture('challenge') != None:
#     print('挑戰任務')
#     pyautogui.click(complete)

# 如果有挑戰任務
#     滑到最左邊
#     確認隊伍
#     選擇terry佔有
#     進關卡
#     開terry
#     完成任務

# 節數領取獎勵
#     如果有挑戰關卡

# 如果沒體力
# 如果鑰匙滿了








