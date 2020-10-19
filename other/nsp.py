A = input().split()
B = []
if len (A) % 2 == 1:
    for i in range (0, len (A) - 1, 2):
        B.append (A[i + 1])
        B.append (A[i])
    B.append ( A[len (A) - 1])
else:
    for i in range (0, len (A), 2):
        B.append (A[i + 1])
        B.append (A[i])
A = B
for j in range (len (A)):
    print (A[j], " ", sep ="", end = "")