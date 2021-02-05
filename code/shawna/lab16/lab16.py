from PIL import Image, ImageEnhance, ImageColor
import colorsys
# ---- Lab 16 ---- #

# -- Conor and Shawna -- #

# - Version 1 - #
# - Convert Image to Greyscale

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

img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        # colorsys uses colors in the range [0, 1]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

        h, s, v = h + 0.9, s + 0.5, v - 0.5

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        r = int(r*255)
        g = int(g*255)
        b = int(b*255)
        
        pixels[i, j] = int(r), int(g), int(b)

img.show()

