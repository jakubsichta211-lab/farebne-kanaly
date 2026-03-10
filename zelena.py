import PIL
from PIL import Image
pic = Image.open("d0105.jpg")
pixels = pic.load()
for y in range(pic.size[1]):
    for x in range(pic.size[0]):
        pixel = pixels[x, y]
        g = pixel[0]
        pixels[x,y] = (0,g,0)
        

pic.show()