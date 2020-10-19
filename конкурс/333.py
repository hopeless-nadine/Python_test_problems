s = 0
k = 0
while 0 == 0:
    n = int (input())
    if n == 0:
        break
    else:
        if n % 11 == 0:
            s = s + n
            k = k + 1
            l = s // k
print (l)