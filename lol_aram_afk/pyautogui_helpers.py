import time

import pyautogui
import pydirectinput


class PyAutoGUIHelpers:
    def __init__(self):
        pass
    # def __init__(self, image_path = 'images/', image_format = '{self.image_format}'):
    #     self.image_path = image_path
    #     self.image_format = image_format

    # 重複找圖片直到找到
    def find_image(self, img_name: str, box: tuple = None, confidence = 0.7, interval = 0):
        image = None
        if interval == 0:
            while image is None:
                image = pyautogui.locateOnScreen(f'{self.image_path}{img_name}{self.image_format}', region=box, confidence=confidence)
        else:
            while image is None:
                image = pyautogui.locateOnScreen(f'{self.image_path}{img_name}{self.image_format}', region=box, confidence=confidence)
                time.sleep(interval)
        return pyautogui.center(image)

    # 尋找圖片並回傳
    # 沒有則 None
    def on_screen(self, img_name: str, box: tuple = None, confidence = 0.7):
        image = pyautogui.locateOnScreen(f'{self.image_path}{img_name}{self.image_format}', region=box, confidence=confidence)
        return pyautogui.center(image)

    # 找圖片並點擊
    def find_and_click(self, img_name: str, box: tuple = None, confidence = 0.7):
        image = pyautogui.locateOnScreen(f'{self.image_path}{img_name}{self.image_format}', region=box, confidence=confidence)
        if image:
            pyautogui.click(image)

    # --------------------------------------------------
    # 其他

    # 滑鼠座標
    def pos():
        last_pos = pyautogui.position()
        try:
            while True:
                #新位置
                new_pos = pyautogui.position()
                if last_pos != new_pos:
                    print(new_pos)
                    last_pos = new_pos
        except KeyboardInterrupt:
            print('\nExit')

    # 等待 n 秒
    def wait(second):
        for s in range(second, 0, -1):
            print(s)
            time.sleep(1)
    
    # 截圖 (根據 Snipaste 座雕)
    def screen_shot(self, img_name: str, box: tuple):
        pyautogui.screenshot(f'{img_name}{self.image_format}', region=(box[0],
                                                   box[1],
                                                   box[2] - box[0] + 1,
                                                   box[3] - box[1] + 1))

