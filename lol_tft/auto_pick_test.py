import time

import pyautogui
import keyboard

from pyautogui_class import LOL

key = 'a'

image_path = 'images/'
card_path = 'cards/'
sign = f'{image_path}sign.png'

# 範圍
all_cards_box = (472, 921, 1012, 159)

card_boxes = [(481, 929, 190, 141),
              (682, 929, 190, 141),
              (883, 929, 190, 141),
              (1085, 929, 190, 141),
              (1286, 929, 190, 141)]

# 左上角的點的y軸
card_boxes_left = [card_box[0] for card_box in card_boxes]
card_boxes_left.append(1500)

# 中心點
card_boxex_center = [pyautogui.center(card_box) for card_box in card_boxes]

want_cards = ["K'Sante", "Aphelios", "Yone", "Sett", "Ezreal", "Kayn"]

def pick_card():
    click_list = []
    for i in range(10, 4, -1):
        confidence = i
        if i == 100:
            print('confidence: None')
            for card in want_cards:
                find_cards_pos = pyautogui.locateAllOnScreen(f'{card_path}{card}.png', region=all_cards_box)

                for pos in find_cards_pos:
                    click_list.append(pos)
                    print(pos)
                    # print(card)

        else:
            print(f'confidence: {confidence}')
            for card in want_cards:
                find_cards_pos = pyautogui.locateAllOnScreen(f'{card_path}{card}.png', region=all_cards_box, confidence=confidence)

                for pos in find_cards_pos:
                    click_list.append(pos)
                    print(pos)
                    # print(card)
            
    print(click_list)
    # [print(click_list) if click_list else None]

    # 點擊
    # for pos in click_list:
    #     # print(pos)
    #     pos_left = pos[0]

    #     for center in card_boxex_center:
    #         if pos_left < center:
    #             # 截圖測試
    #             # pyautogui.screenshot(f'{image_path}{count}_{i}.png', region = (pos[0] - 100, pos[1] - 100, pos[2] + 200, pos[3] + 200))
                
    #             # 移動滑標測試
    #             # pyautogui.moveTo(center)
    #             # time.sleep(1)

    #             click_list.append(card_boxex_center.index(center) + 1)

    #             # LOL.click(center)
    #             break

    # 測試
    # test_output = [f'{i} ' if i in click_list else '  ' for i in range(1, 6)]
    # print(''.join(test_output))
    # print('__________')


if __name__ == '__main__':
    print('.w.')
    try:
        while True:
            keyboard.wait(key)
            time.sleep(0.4)

            pick_card()

    except KeyboardInterrupt:
        print('\nExit')