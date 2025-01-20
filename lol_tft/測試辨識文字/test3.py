import cv2

# 讀取圖片
img1 = cv2.imread("test1.png")
img2 = cv2.imread("test2.png")

# 比對圖片是否完全相同
result = cv2.compare(img1, img2, cv2.CMP_EQ)

# 如果 result 為 0，則兩張圖片完全相同
# print(result)
if (result <= 2).all():
    print("The images are completely equal.")
else:
    print("The images are not equal.")