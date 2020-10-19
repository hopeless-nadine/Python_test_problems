def pologenie (x1, y1, x2, y2, A, B, C):
    if ((A * x1 + B * y1 + C) * (A * x2 + B * y2 + C)) > 0:
        return "YES"
    else:
        return "NO"
print (pologenie (float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input())))
    