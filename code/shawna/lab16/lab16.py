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

from PIL import Image, ImageEnhance, ImageColor
import colorsys

img = Image.open("lenna.png") # must be in same folder
enhancer = ImageEnhance.Sharpness(img)
bright = ImageEnhance.Brightness(img)
color = ImageEnhance.Color(img)
factor = 2
color_factor = 0.3
img2 = enhancer.enhance(factor).show(f"Sharpness {factor}")
img3 = bright.enhance(factor).show(f"Brightness {factor}")
img4 = color.enhance(color_factor).show(f"Color {color_factor}")

