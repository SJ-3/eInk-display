import os
from PIL import Image
from inky.auto import auto

img = Image.open("/home/pi/beach.png")
inky_display.set_image(img)
inky_display.show()
