from PIL import Image, ImageEnhance, ImageColor, ImageDraw
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

# img = Image.open("lenna.png") # must be in same folder
# width, height = img.size
# pixels = img.load()

# for i in range(width):
#     for j in range(height):
#         r, g, b = pixels[i, j]
#         # colorsys uses colors in the range [0, 1]
#         h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

#         h, s, v = h + 0.9, s + 0.5, v - 0.5

#         r, g, b = colorsys.hsv_to_rgb(h, s, v)

#         r = int(r*255)
#         g = int(g*255)
#         b = int(b*255)
        
#         pixels[i, j] = int(r), int(g), int(b)

# img.show()

# - Version 3 - #
# - Draw a SPONGEBOB - #

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

draw.rectangle(((0, 0), (width, height)), fill="white")

draw.rectangle(((150, 100), (350, 260)), fill="yellow", outline="black") # body
draw.rectangle(((190, 326), (200, 400)), fill="yellow", outline="black") # left leg
draw.rectangle(((290, 326), (300, 400)), fill="yellow", outline="black") # right leg

draw.rectangle(((235, 230), (249, 245)), fill="white", outline="black") # left tooth
draw.rectangle(((255, 230), (269, 245)), fill="white", outline="black") # right tooth
draw.rectangle(((150, 100), (350, 325)), fill= None, outline = "black") # full body outline

eh = 3.2
lew = 2.30
rew = 1.75

# Left White Eye
circle_x = width/lew + .5
circle_y = height/eh
circle_radius = 30
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='white', outline='black')

# Left Blue Eye
circle_x = width/lew
circle_y = height/eh
circle_radius = 10
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='darkturquoise', outline='black')

# Left Black Eye
circle_x = width/lew
circle_y = height/eh
circle_radius = 5
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='black', outline='black')

# Right White Eye
circle_x = width/rew
circle_y = height/eh
circle_radius = 30
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='white', outline='black')

# Right Blue Eye
circle_x = width/rew
circle_y = height/eh
circle_radius = 10
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='darkturquoise', outline='black')

# Right Black Eye
circle_x = width/rew
circle_y = height/eh
circle_radius = 5
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='black', outline='black')

# arc for the smile
w, h = 350, 240
shape = [(160, 100), (w - 10, h - 10)]
draw.arc(shape, start = 20, end = 160, fill="black")

draw.rectangle(((150, 275), (350, 325)), fill="saddlebrown", outline="black") # pants
draw.rectangle(((180, 326), (210, 350)), fill="saddlebrown", outline="black") # pants left leg
draw.rectangle(((280, 326), (310, 350)), fill="saddlebrown", outline="black") # pants right leg


draw.rectangle(((160, 280), (180, 287)), fill="black") # belt
draw.rectangle(((190, 280), (210, 287)), fill="black") # belt
draw.rectangle(((220, 280), (240, 287)), fill="black") # belt
draw.rectangle(((250, 280), (270, 287)), fill="black") # belt
draw.rectangle(((280, 280), (300, 287)), fill="black") # belt
draw.rectangle(((310, 280), (330, 287)), fill="black") # belt
draw.rectangle(((340, 280), (350, 287)), fill="black") # belt

draw.rectangle(((180, 401), (210, 430)), fill="black") # left shoe
draw.rectangle(((280, 401), (310, 430)), fill="black") # right shoe

draw.polygon(((240, 261), (250, 285), (260, 261)), fill="red") # tie
draw.polygon(((222, 261), (232, 271), (242, 261)), fill="red", outline = "black") # left lapel
draw.polygon(((258, 261), (268, 271), (278, 261)), fill="red", outline = "black") # left lapel

img.show()