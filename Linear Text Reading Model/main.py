import pytesseract
from PIL import Image

# pytesseract.pytesseract.tesseract_cmd = r"D:\Program_Files_(x86)\PyTesseract"
with open("Invoice Text.txt", "w") as file:
    file.writelines(pytesseract.image_to_string(Image.open('sample2.jpg')))
#
# print(pytesseract.image_to_string('test.jpg'))
#
# print(pytesseract.get_languages(config=''))
#
# print(pytesseract.image_to_string(Image.open('test_img.jpg'), lang='en'))
#
