def IsPointInSquare2(x, y):
    if abs (x) <= 1:
        if  abs (y) <= 1 - abs (x):
            return "YES"
        else:
            return "NO"
    else:
        return "NO"
print (IsPointInSquare2(float(input()),float(input())))