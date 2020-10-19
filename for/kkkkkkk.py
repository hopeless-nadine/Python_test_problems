a = int (input())
b = int (input())
c = a % 2
d = (b + 1) % 2
for i in range (a + c, b + 1 + d, 2):
    print (i, " ", sep = "", end = "")
