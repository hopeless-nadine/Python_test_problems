def power (a, n):    
    if n > 0:
        k = a
        for i in range (1, n):
            k = k * a
        return k
    elif n < 0:
        k = 1
        for i in range (0, -(n)):
            k = k / a
        return k 
    else:
        return 1
        
print (power (float(input()), int (input())))