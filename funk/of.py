def pos (n):
    if n == 0:
        return 0
    else:
        a = int (input())
        if a == 0:
            return n
        else:
            return pos (a + n)
print (pos (int(input())))
            