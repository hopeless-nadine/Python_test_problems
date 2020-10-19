A = input().split()
B = []
k = 0
s = 0
for i in range(len(A)):
    A[i] = int(A[i])
    if A[i] > A[k]:
        k = i
for j in range(len(A)):
    A[j] = int(A[j])
    if A[j] < A[s]:
        s = j
for n in range (len (A)):
    if A[n] == A[k]:
        B.append (A[s])
    elif A[n] == A[s]:
        B.append (A[k])
    else:
        B.append (A[n])
A = B
for l in range (len (A)):
    print (A[l], " ", sep ="", end = "")