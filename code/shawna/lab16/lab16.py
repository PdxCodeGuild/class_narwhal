# ---- Lab 16 ---- #

# -- Conor and Shawna -- #

# - Version 1 - #
# - Convert Image to Greyscale

# from PIL import Image
# import colorsys

# img = Image.open("lenna.png") # must be in same folder
# width, height = img.size
# pixels = img.load()

# for i in range(width):
#     for j in range(height):
#         r, g, b = pixels[i, j]

#         y = 0.299*r + 0.587*g + 0.114*b
        
#         pixels[i, j] = int(y), int(y), int(y)

# img.show()

# - Version 2 -#
# - Increase Saturation, Decrease Brightness and Rotate Hue - #

from PIL import Image, ImageEnhance
import colorsys

img = Image.open("lenna.png") # must be in same folder
#width, height = img.size
# lenna = img.load()

enhancer = ImageEnhance.Sharpness(img)
for i in range(8):
    factor = i / 4.0
    enhancer.enhance(factor).show(f"Sharpness {factor}")
    # contrast = ImageEnhance.Contrast(img)
    # contrast.enhance(4.0).save('img.png')

# img2 = Image.open('img.png')
# img2.show()
img.show()