a = int (input ())
b = int (input ())
c = int (input ())
d = int (input ())
if a % 2 == c % 2:
    if b == d:
        print ("YES")
    if b == d + 2:
        print ("YES")
    if b == d - 2:
        print ("YES")
    if b == d + 4:
        print ("YES")
    if b == d - 4:
        print ("YES")  
    if b == d + 6:
        print ("YES")
    if b == d - 6:
        print ("YES") 
    else:
        print ("NO")
else:
    if b == d + 1:
        print ("YES")
    if b == d - 1:
        print ("YES")
    if b == d + 3:
        print ("YES")
    if b == d - 3:
        print ("YES")  
    if b == d + 5:
        print ("YES")
    if b == d - 5:
        print ("YES")
    if b == d + 7:
        print ("YES")
    if b == d - 7:
        print ("YES")
    else:
        print ("NO")        
