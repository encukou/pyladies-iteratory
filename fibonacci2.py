def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = a + b, a


for f in fibonacci():
    print f
    if f > 10:
        break
