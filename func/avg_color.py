def avg_color(colors: list|tuple) -> list:
    avregd_colors = []
    for block_of_colors in colors:
        r = []
        g = []
        b = []
        for color in block_of_colors:
            r.append(color[0])
            g.append(color[1])
            b.append(color[2])
        r_avg = int(sum(r)/len(r))
        g_avg = int(sum(g)/len(g))
        b_avg = int(sum(b)/len(b))
        
        avregd_colors.append((r_avg,g_avg,b_avg))
    return avregd_colors