n = int (input ())
m = int (input ())
k = int (input ())
if n * m > k:
    if (n * m - k) % n == 0:
        print ("YES")
    elif (n * m - k) % m == 0:
        print ("YES")
    else:
        print ("NO")
else:
    print ("NO")
    
