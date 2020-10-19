A = input().split()
s = 0 
for i in range(len(A)):
    A[i] = int(A[i])
    if A[i] > 0:
        while A[s] <= 0:
            s = s + 1
        if A[i] < A[s]:
            s = i
print (A[s])