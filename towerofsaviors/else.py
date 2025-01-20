# 公會座標
# guild = (point1[0] + 85, point1[1] + 650)

# print(pyautogui.position())

# 開始自走銅鑼座標
auto = (point1[0] + 100, point1[1] + 30)

# 敵人資訊座標
target = (point1[0] + 280, point1[1] + 250)

def play():
    pyautogui.click(auto)

def stop():
    pyautogui.click(auto)

def information():
    pyautogui.mouseDown(target)
    time.sleep(0.5)
    pyautogui.mouseUp(target)

def fight():
    # 第一關
    find_picture('e1')
    print('----------第一關----------')

    stop()

    print('紅綠燈 手消5c')

    # 第二關
    find_picture('e2')
    print('----------第二關----------')

    play()

    # 第三關
    # find_picture('e3')
    print('----------第三關----------')

    # 第四關
    # find_picture('e4')
    print('----------第四關----------')

    # 第五關
    # find_picture('e5')
    print('----------第五關----------')
    
    print('自己轉')

    # 第六關
    print('----------第六關----------')