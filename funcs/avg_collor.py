from PIL import Image
from funcs.rgba_of_pixel import rgba_of_pixel

def avg_collor(image: Image, x_list: list|tuple, y_list: list|tuple) -> list[int,int,int]|bool:
    width = image.width
    height = image.height

    r_list = []
    g_list = []
    b_list = []

    for y in y_list:
        for x in x_list:
            rgba = rgba_of_pixel(image, x, y)

            if rgba[3] == 255:
                r_list.append(rgba[0])            
                b_list.append(rgba[1])            
                g_list.append(rgba[2])
            else:
                return False

    return (int(sum(r_list)/len(r_list)),  int(sum(g_list)/len(g_list)), int(sum(b_list)/len(b_list)))            
