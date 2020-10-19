a = int (input ())
if a % 4 == 0:    
    if a % 100 == 0 and not (a % 400 == 0):
        print ("NO")
    else: 
        print ("YES")
else:
    print ("NO")