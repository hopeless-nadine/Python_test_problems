A = input().split()
x = int (input ()) 
for i in range(len(A)):
    A[i] = int(A[i])
    if A[i] < x:
        a = i + 1
        break
if int (A[len(A) - 1]) > x:
    a = len (A) + 1
elif len (A) == 1:
    if A[0] < x:
        a = 1
    else:
        a = 2
print (a)