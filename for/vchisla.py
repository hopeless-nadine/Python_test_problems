a = int (input())
b = int (input())
if a < b:
    for i in range (a, b + 1):
        c = i // 1000
        d = (i % 1000)//100
        e = (i % 100) // 10
        f = i % 10
        if c == d:
            if c == e and not (c == f):
                print (i)
            elif c == f and not (c == e):
                print (i)
        elif c == e:
            if c == d and not (c == f):
                print (i)
            elif c == f and not (c == d):
                print (i)  
        elif c == f:
            if c == d and not (c == e):
                print (i)
            elif c == e and not (c == d):
                print (i) 
        elif d == e:
            if d == c and not (d == f):
                print (i)
            elif d == f and not (d == c):
                print (i) 
        elif d == f:
            if d == c and not (d == e):
                print (i)
            elif d == e and not (d == c):
                print (i)   
        elif f == e:
            if f == c and not (f == d):
                print (i)
            elif f == d and not (c == f):
                print (i)         
        
            
else:
    for i in range (a, b + 1):
        c = i // 1000
        d = (i % 1000)//100
        e = (i % 100) // 10
        f = i % 10
        if c == d:
            if c == e and not (c == f):
                print (i)
            elif c == f and not (c == e):
                print (i)
        elif c == e:
            if c == d and not (c == f):
                print (i)
            elif c == f and not (c == d):
                print (i)  
        elif c == f:
            if c == d and not (c == e):
                print (i)
            elif c == e and not (c == d):
                print (i) 
        elif d == e:
            if d == c and not (d == f):
                print (i)
            elif d == f and not (d == c):
                print (i) 
        elif d == f:
            if d == c and not (d == e):
                print (i)
            elif d == e and not (d == c):
                print (i)   
        elif f == e:
            if f == c and not (f == d):
                print (i)
            elif f == d and not (c == f):
                print (i) 