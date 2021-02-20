from PIL import Image
img = Image.open("F_Douglass.jpeg") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        y = 0.299*r + 0.587*g + 0.114*b

        r = y
        g = y
        b = y
        
        r = int(r)
        g = int(g)
        b = int(b)
        
        pixels[i, j] = (r, g, b)

img.show()