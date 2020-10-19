def st (a, n):
    if n % 2 == 0:
        if n == 1:
            return a
        else:
            return ((a ** 2) ** (n - 2)/2) * (a ** 3)
print (st (float (input()), int (input())))