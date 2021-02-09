from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill="white")

# using the color light brown
color = (130, 93, 74)  # light brown


# arms
draw.line((75, 300, 165, 160), width=30, fill=color)
draw.line((335, 160, 425, 300), width=30, fill=color)

# shirt
# draw a rectangle from x0, y0 to x1, y1
draw.rectangle(((150, 125), (350, 375)), fill="lightblue")

# sleeves
draw.line((138, 200, 162, 160), width=30, fill="lightblue")
draw.line((338, 160, 362, 200), width=30, fill="lightblue")

# buttons
circle_x = 250
circle_y = 160
circle_radius = 5
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='black')

circle_x = 250
circle_y = 210
circle_radius = 5
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='black')

circle_x = 250
circle_y = 260
circle_radius = 5
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='black')

# belt
draw.line((150, 325, 350 , 325), width=25, fill="brown")
draw.line((240, 325, 260, 325), width=31, fill="gold")
draw.rectangle(((243,318, 257, 332)), fill="brown")

# legs
draw.line((175, 375, 175, height), width=50, fill="darkblue")
draw.line((325, 375, 325, height), width=50, fill="darkblue")


# head
circle_x = 250
circle_y = 75
circle_radius = 50
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill=color)

# eyes
circle_x = 230
circle_y = 60
circle_radius = 5
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='white')

circle_x = 270
circle_y = 60
circle_radius = 5
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='white')

draw.line((230, 95, 270, 95), width=5, fill="pink")


img.show()