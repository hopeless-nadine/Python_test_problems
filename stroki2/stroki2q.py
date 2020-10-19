A = input().split()
k = int (input())
print (' '.join(A[:k] + A[k + 1:len(A)]))
