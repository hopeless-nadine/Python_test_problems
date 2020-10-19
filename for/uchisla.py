a = int (input())
b = int (input())
if a < b:
    for i in range (a, b + 1):
        c = i // 1000
        d = (i % 1000)//100
        e = (i % 100) // 10
        f = i % 10
        if c == f and d == e:
            print (i)
else:
    for i in range (b, a + 1):
        c = i // 1000
        d = (i % 1000)//100
        e = (i % 100) // 10
        f = i % 10
        if c == f and d == e:
            print (i)        