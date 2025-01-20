import os

def are_images_equal(image1_path, image2_path):
    # 讀取兩張圖片的二進位數據
    with open(image1_path, 'rb') as img1_file:
        img1_data = img1_file.read()

    with open(image2_path, 'rb') as img2_file:
        img2_data = img2_file.read()

    # 比較二進位數據
    return img1_data == img2_data


def find_matching_image(target_image_path, folder_path):
    for filename in os.listdir(folder_path):
        current_image_path = os.path.join(folder_path, filename)
        if os.path.isfile(current_image_path):
            if are_images_equal(target_image_path, current_image_path):
                return filename
    return False

# 測試
if __name__ == '__main__':
    target_image_path = "test1.png"
    folder_path = "cards"

    if find_matching_image(target_image_path, folder_path):
        print("目標圖片和資料夾中的某張圖片相同。")
    else:
        print("目標圖片與資料夾中的所有圖片都不相同。")
