a = int(input(''))
b = int(input(''))
c = int(input(''))
if a <= b:
    if a >= c:
        print(a)
if a >= b:
    if a<=c:
        print(a)
if b <= a:
    if b >= c:
        print(b)
if b >= a:
    if b<=c:
        print(b)
if c <= a:
    if c >= b:
        print(c)
if c >= a:
    if c<=b:
        print(c)