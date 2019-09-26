def fac(n):
    if n == 1:
        return 1
    else:
        return n + fac(n-1)


def dirReduc(a):
    dir = {"NORTH": "SOUTH", "SOUTH": "NORTH", "WEST": "EAST", "EAST": "WEST"}
    for i, d in enumerate(a):
        if i == len(a) - 1:
            return a
        if d == dir[a[i+1]]:
            a.pop(i+1)
            a.pop(i)
            return dirReduc(a)
