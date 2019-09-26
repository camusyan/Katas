def increment_string(s):
    import re
    r = re.match('^([\d]+)(.*)$', s[::-1])
    n = '' if r is None else r.group(1)[::-1]
    return s + '1' if r is None else r.group(2)[::-1] + '0' * (len(n) - len(str(int(n)+1))) + str(int(n)+1)

def primeFactors(n):
    from math import sqrt
    p = {}
    for i in range(2, int(sqrt(n))):
        while n % i == 0 and n > 1:
            p[i] = 1 if i not in p else p[i] + 1
            n /= i
        if n == 1:
            break
    if n != 1:
        p[int(n)] = 1
    s = ''
    for i in sorted(p.keys()):
        s += '(' + str(i) + '**' + str(p[i]) + ')' if p[i] > 1 else '(' + str(i) + ')'

    return s

def spiralize(n):
    import numpy as np
    m = np.zeros([n,n]).astype(int)
    r=c=rot=0
    while True:
        if c == n-1:
            m[r, c] = c = 1
            m = np.rot90(m)
            rot += 1
        elif m[r, c+1] == 0 and m[r+1, c+1] == 0:
            m[r, c] = 1
            c += 1
        else:
            c_ = c
            c = r
            r = n - c_
            m = np.rot90(m)
            rot += 1
        if r > n / 2:
            break
    while rot % 4 != 0:
        m = np.rot90(m)
        rot += 1
    return m.tolist()
