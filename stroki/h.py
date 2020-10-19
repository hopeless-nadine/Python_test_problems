A = input().split()
s = 0
for i in range(len(A)):
    A[i] = int(A[i])
    if A[i] > 0:
        if A[s] > 0:
            if A[i] < A[s]:
                s = i    
        else:
            s = s + 1
print (A[s])


        