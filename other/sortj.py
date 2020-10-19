n = int (input())
A =[]
B =[]
for i in range (n):
    Q = input().split()
    A.append (Q[0])
    B.append (Q[1])
for g in range (len (A)):
    B[g] = int (B[g])
for l in range (len (B) - 1):
    for j in range (len (B) - 1 - l):
        if B[j] < B[j + 1]:
            B[j], B[j + 1] = B[j + 1], B[j] 
            A[j], A[j + 1] = A[j + 1], A[j]
for k in range (len (A)):
    print (A[k],sep = "")
    
    