import PIL
from PIL import Image
pic = Image.open("d0105.jpg")
pixels = pic.load()
for y in range(pic.size[1]):
    for x in range(pic.size[0]):
        pixel = pixels[x, y]
        r = pixel[0]
        pixels[x,y] = (r,0,0)
        

pic.show()