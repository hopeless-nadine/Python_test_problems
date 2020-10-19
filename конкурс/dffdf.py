N = int (input())
A = input().split()
for i in range (0, N):
    if int (A[i]) % 7 == 0:
        print (A[i], " ", sep ="", end ="")
        
        