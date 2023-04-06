from PIL import Image
img = Image.open("assets/MainCharacters/MaskDude/idle.png")
x, y = img.size
print(x,y)
print(x//2,y//2)