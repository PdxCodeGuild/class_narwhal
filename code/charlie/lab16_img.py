from PIL import Image
img = Image.open("F_Douglass.jpg") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        r *= 0.299
        g *= 0.587
        b *= 0.114 
        r = int(r)
        g = int(g)
        b = int(b)
        #Y = 0.299*R + 0.587*G + 0.114*B
        pixels[i, j] = (r, g, b)

img.show()