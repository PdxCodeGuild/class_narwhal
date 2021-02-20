from playsound import playsound
playsound('the_warcry.mp3',False)
from PIL import Image, ImageOps
import random 
import time 


img = Image.open("BP.png")
img2 = ImageOps.grayscale(img)
img2.save("grayscale.png")
width, height = img.size
pixels = img2.load()
img3 = Image.open("ironman3_2.png")
img4 = Image.open("vinmcu.png")
img5 = Image.open("iron_spi.png")
img6 = Image.open("cap_am.png")
img7 = Image.open("fal_buck.png")
img8 = Image.open("hawk_ron.png")  
img9 = Image.open("ant_man.png")


Civil_War = ["ironman3_2.png","vinmcu.png","iron_spi.png","cap_am.png","fal_buck.png","hawk_ron.png","ant_man.png",
"Bp.png"]



counter = 0
  
  
while counter < len(Civil_War):
    img = Image.open(Civil_War[counter % len(Civil_War)])
    img.show()
    counter +=1
    time.sleep(1)
    
    
   

