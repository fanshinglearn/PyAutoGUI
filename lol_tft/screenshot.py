# 截圖小程式

import pyautogui
import time
import os
import shutil

import tkinter as tk
from PIL import Image,ImageTk

import equal_images

# 新版本卡總數
total_cards = 13 + 13 + 13 + 13 + 8
    
root = tk.Tk()

root.geometry("1100x300+300+100")
root.resizable(0,0)
root.title('測試截圖')
# root.configure(bg='#a0abff')

# 範圍
card_boxes = [(481, 929, 190, 141),
              (682, 929, 190, 141),
              (883, 929, 190, 141),
              (1085, 929, 190, 141),
              (1286, 929, 190, 141)]

# (473, 922, 1009, 154)

image_path = 'images/'
card_path = 'cards/'

font = ("TkDefaultFont", 12)
green_hex = '#80f24b'
red_hex = '#f20505'
yello_hex = '#fff119'
initial_img = ImageTk.PhotoImage(file=f'{image_path}black.png')

def count_screenshot_cards():
    # 獲取資料夾中的檔案清單
    images = os.listdir(card_path)

    # 計算檔案數量
    num_cards = len(images)

    L.config(text=f'已截圖 {num_cards} / {total_cards}')


# 截圖按鈕
def screenshot():
    global img
    img = []
    for i in range(5):
        # 清空輸入文字
        E[i].delete(0, 'end')

        screenshot_img_path = f'{image_path}{i}.png'

        # 截圖
        pyautogui.screenshot(screenshot_img_path, region = card_boxes[i])

        # 加入截圖圖片
        img.append(ImageTk.PhotoImage(file=screenshot_img_path))
        img_label[i].config(image=img[i])

        # 是否已截過圖
        equal_image = equal_images.find_matching_image(screenshot_img_path, card_path)
        if equal_image:
            img_name, extension = os.path.splitext(equal_image)
            img_name_label[i].config(text=img_name, bg=green_hex)
        else:
            img_name_label[i].config(text='? ? ?', bg=red_hex)
        
        count_screenshot_cards()



# 儲存按鈕
def save():
    for i in range(5):
        if E[i].get() != '':
            if f'{i}.png' in os.listdir(image_path):
                if f'{E[i].get()}.png' not in os.listdir(card_path):
                    shutil.copyfile(f'{image_path}{i}.png', f'{card_path}{E[i].get()}.png')
                    img_name_label[i].config(text=E[i].get(), bg=green_hex)
                else:
                    img_name_label[i].config(text='已有重複名稱!!', bg=yello_hex)
    
    count_screenshot_cards()


# 關掉時刪除截圖
def on_closing():
    for i in range(5):
        img_path = f'{image_path}{i}.png'
        if os.path.exists(img_path):
            os.remove(img_path)

    root.destroy()


# 按鈕
B1=tk.Button(root, text='截圖', command=screenshot, font=font)
B1.pack()

# 框架
F=tk.LabelFrame(root, text='圖片', font=font, padx=10, pady=10)
F.pack()

# img_frame = []
E = []
img_label = []
img_name_label = []

for i in range(5):
    # 創建五個小框架，裡面有文字標籤和圖片標籤
    frame=tk.Frame(F)
    frame.pack(side='left')
    # img_frame.append(frame)

    # 上文字方塊
    Entry = tk.Entry(frame, font=font, justify='center')
    Entry.pack()
    E.append(Entry)

    # 中圖片標籤
    label = tk.Label(frame, image=initial_img)
    label.pack()
    img_label.append(label)

    # 名稱標籤
    label = tk.Label(frame)
    label.pack()
    img_name_label.append(label)

B2=tk.Button(root, text='儲存', command=save, font=font)
B2.pack()

L = tk.Label(root)
L.pack(side='right')

# 設置視窗關閉事件的處理函數
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
