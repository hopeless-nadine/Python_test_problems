def sum (a, b):
    if a == 0:
        return b
    else:
        return 1 + 1 + sum (a - 1, b - 1)
print (sum (int (input()), int (input ()))) 
