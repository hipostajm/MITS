from PIL import Image


def rgba_of_pixel(image: Image, x: int, y: int) -> tuple[int, int, int, int]:  # Image needs to be converted with .convert('RGBA')
    r, g, b, a = image.getpixel((x, y))
    return (r, g, b, a)
