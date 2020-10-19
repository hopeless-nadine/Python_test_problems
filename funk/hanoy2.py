def hanoy2 (n, x, y, m):
    if n == 1:
        print (1, x, m)
        print (1, m, y)
    else:
        hanoy2 (n - 1, x, y, m)
        print (n, x, m)
        hanoy2 (n - 1, y, x, m)
        print (n, m, y)
        hanoy2 (n - 1, x, y, m)
hanoy2(int(input()), 1, 3, 2)