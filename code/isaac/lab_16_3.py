from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill="white")

# draw a rectangle from x0, y0 to x1, y1
draw.rectangle(((150, 125), (350, 375)), fill="lightblue")

# draw a line from x0, y0, x1, y1
# using the color pink
color = (256, 128, 128)  # pink
draw.line((75, 200, 150, 200), fill=color)
draw.line((350, 200, 425, 200), fill=color)
draw.line((150, 375, 150, height), fill=color)
draw.line((350, 375, 350 , height), fill=color)



circle_x = 250
circle_y = 75
circle_radius = 50
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')

img.show()