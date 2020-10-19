a = int (input ())
b = int (input ())
c = int (input ())
if a + b > c:
    if b + c > a:
        if a + c > b:
            print ("YES")
        else:
            print ("NO")
    else:
        print ("NO")
else:
    print ("NO")