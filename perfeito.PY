p = 1
while p <= 40000000:
    d = 1
    q = 0
    while (p!=d):
        if (p%(d/2) == 0):
            q = q+d
        d += 1
    if q == p:
        print(p)
    p += 1
    