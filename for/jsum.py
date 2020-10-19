n = int (input())
s = 0
for i in range (2, n):
    s = s + i * (i - 1)
    print (i - 1, "*", i, "+", sep ="", end ="")
s = s + n * (n - 1)
print (n - 1, "*", n, "=", s, sep ="")
    
