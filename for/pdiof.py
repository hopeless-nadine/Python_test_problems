a = int (input())
b = int (input())
c = int (input())
d = int (input())
e = int (input())
s = 0
for i in range (0, 1001):
    if not (i - e ) == 0:
        if (a * (i ** 3 ) + b * (i ** 2) + c * i + d)/(i - e) == 0:
            s = s + 1
print (s)
        