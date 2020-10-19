def C (n, k):
    if k == 0:
        return 1
    elif k == n:
        return 1
    else:
        return C (n - 1, k) + C (n - 1, k - 1)
print (C (int(input()), int (input())))
    