def hanoy (n, x, y, m):
    if n == 1:
        print(1, x, y)
    else:
        hanoy (n - 1, x, m, y)
        print (n, x, y)
        hanoy (n - 1, m, y, x)
hanoy (int(input()), 1, 3, 2)

            