a = int (input ())
b = int (input ())
c = int (input ())
d = int (input ())
if a == c:
    if b == d + 1:
        print ("YES")
    if b == d - 1:
        print ("YES")
    else:
        print ("NO")
elif b == d:
    if a == c + 1:
        print ("YES")
    if a == c - 1:
        print ("YES")
    else:
        print ("NO")
elif a == c + 1:
    if b == d + 1:
        print ("YES")
    if b == d - 1:
        print ("YES")
    else:
        print ("NO")   
elif a == c - 1:
    if b == d + 1:
        print ("YES")
    if b == d - 1:
        print ("YES")
    else:
        print ("NO")
else:
    print ("NO")