n = int (input())
A = []
B = []
C = []
for i in range (n):
    A.append (int (input()))
    B.append (int (input()))
    C.append (int (input()))
for g in range (len (A)):
    A[g] = int (A[g])
    B[g] = int (B[g])
    C[g] = int (C[g])
for l in range (len (A) - 1):
    for j in range (len (A) - 1 - l):
        if C[j] > C[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
            B[j], B[j + 1] = B[j + 1], B[j]
            C[j], C[j + 1] = C[j + 1], C[j]
for l in range (len (B) - 1):
    for j in range (len (B) - 1 - l):
        if B[j] > B[j + 1]:
            B[j], B[j + 1] = B[j + 1], B[j]
            A[j], A[j + 1] = A[j + 1], A[j]
            C[j], C[j + 1] = C[j + 1], C[j]
for l in range (len (B) - 1):
    for j in range (len (B) - 1 - l):
        if A[j] > A[j + 1]:    
            B[j], B[j + 1] = B[j + 1], B[j]
            A[j], A[j + 1] = A[j + 1], A[j]
            C[j], C[j + 1] = C[j + 1], C[j]
for k in range (len (A)):
    print (A[k], " ", B[k], " ", C[k], sep = "")
    

