import pyautogui
import time

pyautogui.FAILSAFE = True

# 自走銅鑼座標
find = [1414, 484]

# 夜神模擬器左上右下座標
point1 = (find[0] - 203, find[1] - 436)
point2 = (552, 980)
box = point1 + point2

center = (point1[0] + (point2[0] / 2), point1[1] + (point2[1] / 2))


# 尋找圖片 回傳座標
def find_picture(img):
    picture = pyautogui.locateOnScreen('%s.png'%img, region=box, confidence=0.6)
    return picture

# 尋找圖片 並點擊
def find_and_click(img):
    picture = find_picture(img)
    pyautogui.click(picture)

# 每秒找一次圖直到找到
def until_find_picture(img):
    while True:
        picture = find_picture(img)
        if picture != None:
            break
        else:
            time.sleep(1)

def wait(second):
    for s in range(second, 0, -1):
        print(s)
        time.sleep(1)

# n = input('打幾次')
n = 3

wait(3)

for i in range(1, n+1):
    # 案確定開始
    print('尋找並點擊enter')
    find_and_click('enter')
    wait(10)

    # 點Terry
    print('尋找Terry中...')
    until_find_picture('terry')
    print('找到了Terry了!')
    wait(5)
    print('開Terry技能')
    find_and_click('terry')
    wait(10)

    # 通關
    print('尋找通關圖片中...')
    until_find_picture('finish')
    print('找到了!')
    wait(1)
    print('點擊正中間')
    pyautogui.click(center)
    wait(1)

    # 再一次
    print('再來一次')
    find_and_click('again')
    wait(3)




