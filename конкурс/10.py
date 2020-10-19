N = int (input())
A = input().split()
k = 0
for i in range (1, len(A)):
    if (((int (A[i])) * (int (A[i - 1])) > 0) and (int (A[i - 1]) % 6 == 0) and (int (A[i]) % 6 == 0)):
        k = 1
        print ("YES")
        break
if k == 0:
    print ("NO")