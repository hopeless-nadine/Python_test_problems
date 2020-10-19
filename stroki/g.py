A = input().split()
s = 0 
k = 0
for i in range(len(A)):
    A[i] = int(A[i])
    if A[i] > A[s]:
        s = i
print (A[s], s)
    
            
           