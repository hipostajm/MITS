from PIL import Image


def rgb_of_pixel(image: Image, x: int, y: int) -> tuple[int, int, int]:
    r, g, b = image.getpixel((x, y))
    rgb = (r, g, b)
    return rgb
