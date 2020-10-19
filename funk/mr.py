def phib (n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return phib (n - 1) + phib (n - 2)
print (phib (int (input())))