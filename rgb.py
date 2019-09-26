def rgb(r, g, b):
    r, g, b = [0 if x<0 else 255 if x>255 else x for x in [r, g, b]]
    return '{:02x}{:02x}{:02x}'.format(int(hex(r)[2:].upper(), 16), int(hex(g)[2:].upper(), 16), int(hex(b)[2:].upper(), 16))
