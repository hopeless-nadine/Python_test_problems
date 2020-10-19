a = input().split()
b = set()
c = set()
for i in range (int (a[0])):
    x = int (input())
    b.add (x)
for l in range (int (a[1])):
    y = int (input())
    c.add (y)
print (len (b.intersection(c)))
print (*sorted (b.intersection(c)))
print (len (b.difference(c)))
print (*sorted (b.difference(c)))
print (len (c.difference(b)))
print (*sorted (c.difference(b)))    

 
