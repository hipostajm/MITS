import PIL
import PIL.Image

def test(path,x,y):
    img = PIL.Image.open(path).convert('RGB')
    r, g ,b = img.getpixel((x,y))
    a = (r,g,b)
    return a

imige = 'blend.png'

print(test(imige,1,0))