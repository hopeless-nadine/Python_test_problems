A = input().split()
for i in range (0, len (A) - 1):
    print (int (A[i - 1]) + int (A[i + 1]), " ", sep ="", end ="")
print (int (A[-2]) + int(A[0])) 