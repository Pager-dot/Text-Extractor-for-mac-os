import os
from PIL import ImageGrab, Image
import pyperclip
import pytesseract

img = ImageGrab.grabclipboard()
img.save('/Users/paritosh/Desktop/screenshot.jpg')

a = pytesseract.image_to_string(Image.open('/Users/paritosh/Desktop/screenshot.jpg'))
pyperclip.copy(a)

os.remove('/Users/paritosh/Desktop/screenshot.jpg')