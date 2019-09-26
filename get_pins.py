a = {0: [8],
     1: [2, 4],
     2: [1, 3, 5],
     3: [2, 6],
     4: [1, 5, 7],
     5: [2, 4, 6, 8],
     6: [3, 5, 9],
     7: [4, 8],
     8: [5, 7, 9, 0],
     9: [6, 8],
     }

def get_pins(p):
    pins = [p]
    for i,j in enumerate(p):
        for k in range(0, len(pins)):
            pins += ['{}{}{}'.format(pins[k][:i],x,pins[k][i+1:]) for x in a[int(pins[k][i])]]
    return pins

