from PIL import Image
from funcs.rgba_of_pixel import rgba_of_pixel

def avg_color(image: Image, x_range: list|tuple, y_range: list|tuple) -> list[int,int,int]|bool:
    r_list = []
    g_list = []
    b_list = []

    for y in range(y_range[0], y_range[1]):
        for x in range(x_range[0], x_range[1]):
            rgba = rgba_of_pixel(image, x, y)

            if rgba[3] == 255:
                r_list.append(rgba[0])            
                b_list.append(rgba[1])            
                g_list.append(rgba[2])
            else:
                return False

    return (int(sum(r_list)/len(r_list)),  int(sum(g_list)/len(g_list)), int(sum(b_list)/len(b_list)))            
