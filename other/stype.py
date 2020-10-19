a = int (input ())
b = int (input ())
c = int (input ())
if a + b > c:
    if b + c > a:
        if a + c > b:
            if a ** 2 + b ** 2 == c ** 2:
                print ("rectangular")
            elif a ** 2 + c ** 2 == b ** 2:
                print ("rectangular")
            elif b ** 2 + c ** 2 == a ** 2:
                print ("rectangular")
            elif a ** 2 + b ** 2 > c ** 2 and not (a ** 2 + b ** 2 == c ** 2) and not (a ** 2 + c ** 2 == b ** 2) and not (b ** 2 + c ** 2 == a ** 2): 
                if b ** 2 + c ** 2 > a ** 2:       
                    if a ** 2 + c ** 2 > b ** 2:
                        print ("acute") 
                    else:
                        print ("obtuse") and not (a ** 2 + b ** 2 == c ** 2) and not (a ** 2 + c ** 2 == b ** 2) and not (b ** 2 + c ** 2 == a ** 2)
                else:
                    print ("obtuse") and not (a ** 2 + b ** 2 == c ** 2) and not (a ** 2 + c ** 2 == b ** 2) and not (b ** 2 + c ** 2 == a ** 2)
            else:
                print ("obtuse") and not (a ** 2 + b ** 2 == c ** 2) and not (a ** 2 + c ** 2 == b ** 2) and not (b ** 2 + c ** 2 == a ** 2)
        else:
            print ("impossible")
    else:
        print ("impossible")
else:
    print ("impossible")