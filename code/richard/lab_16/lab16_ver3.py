'''
Josh Novac
Lab 16
Ver_3
Python
PDX Code Guild
'''


'''//////////////////////////////////DIRECTIONS//////////////////////////////////
Pillow can also be used to draw, the code below demonstrates some functions that Pillow provides. 
Use these functions to draw a stick figure.
'''


'''////////CODE////////'''
from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner
# draw a rectangle from x0, y0 to x1, y1

## background
draw.rectangle(((0, 0), (width, height)), fill="white")
## arms
draw.rectangle(((50, 200), (450, 225)), fill="pink")
## left leg
draw.rectangle(((150, 300), (200, 500)), fill="pink")
## right leg
draw.rectangle(((300, 300), (350, 500)), fill="pink")
## body
draw.rectangle(((150, 150), (350, 350)), fill="lightblue")

# draw a line from x0, y0, x1, y1
# using the color pink
'''
color = (256, 128, 128)  # pink
draw.line((0, 0, width, height), fill=color)
draw.line((0, height, width, 0), fill=color)
'''

## head
circle_x = width/2
circle_y = height/5
circle_radius = 60
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')

img.show()