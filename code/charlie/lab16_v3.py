from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill="white")

# draw a rectangle from x0, y0 to x1, y1
draw.rectangle(((220, 150), (280, 350)), fill="lightblue")
draw.rectangle(((100, 200), (220, 212)), fill="magenta")
draw.rectangle(((280, 200), (400, 212)), fill="orange")
draw.rectangle(((220, 350), (232, 501)), fill="yellow")
draw.rectangle(((268, 350), (280, 500)), fill="yellow")
#draw.arc((200, 250))

# draw a line from x0, y0, x1, y1
# using the color pink
color = (256, 128, 128)  # pink
draw.line((0, 0, width, height), fill=color)
draw.line((0, height, width, 0), fill=color)


circle_x = width/2
circle_y = height/4
circle_radius = 60
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')

img.show()