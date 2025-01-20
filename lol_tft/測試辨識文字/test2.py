from PIL import Image, ImageTk
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
config = "test.txt"

img = Image.open('test.png')
text = pytesseract.image_to_string(img, lang='chi_tra',)
print(text)

# print('---------------------------------')
# gray_image = img.convert('L')
# text = pytesseract.image_to_string(gray_image, lang='chi_tra', config=config)
# print(text)

# gray_image = img.convert('L')
# binary_image = gray_image.convert('1')
# binary_image.save('binary_image_2.png')

im = im.crop((30, 60, 100, 110))