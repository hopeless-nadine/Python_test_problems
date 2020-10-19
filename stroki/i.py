A = input().split()
s = 0 
for i in range(len(A)):
    A[i] = int(A[i])
    if A[i] % 2 == 1:
        while A[s] % 2 == 0:
            s = s + 1
        if A[i] < A[s]:
            s = i
if A[s] % 2 == 0:
    print (0)
else:
    print (A[s])