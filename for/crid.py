n = int (input())
a = 10 ** n - 1
b = 10 ** (n - 1)
for i in range (a, b - 1, - 2):
        print (i, " ", end = "")