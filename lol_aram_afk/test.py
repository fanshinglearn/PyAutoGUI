import pyautogui
import pydirectinput
import time


welcome = (817, 139, 278, 34)

find_name1 = (700, 310, 60, 340)
find_name2 = (1270, 310, 60, 340)
color = ''

blue_castle = (1576, 1002)
red_castle = (1847, 742)

hp = (681, 1029, 414, 17)


count = 1

def testbox(box):
    pyautogui.moveTo(box[0], box[1])
    time.sleep(1)
    pyautogui.moveTo(box[0] + box[2], box[1] + box[3])
    time.sleep(1)

def shotbox(box, count):
    pyautogui.screenshot('screenshont/' + str(count) + '.png', region=box)

time.sleep(3)
# shotbox(welcome, 1)
# shotbox(find_name1, 2)
# shotbox(find_name2, 3)
# shotbox(hp, 4)
