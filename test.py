from PIL import Image
from rich_pixels import Pixels
from rich.console import Console
import time



img = Image.open("assets\MainCharacters\MaskDude\idle.png")
x, y = img.size
left = 0
hel=320
console = Console()
def test():
    global x,left,hel
    im1 = img.crop((left,0,x-hel,y-0))
    im1.resize((25,25))
    #im1.show()
    
    
    
    xels = Pixels.from_image(im1)
    console.print(xels,end='\r')
    console.print(end= '\x1b[2K')
    
   
    if hel ==0:
        hel =320
    if left ==320:
        left = 0
    
    hel-=32
    left+=32
    
    #print(hel,left)
    
    
#for i in range(80):
while True:
    test()
    time.sleep(.18333)
    console.clear()