p = int (input ())
x = int (input ())
y = int (input ())
h = 1 + (p / 100)
k = x +  y / 100
n = h * k
a = round  (n)
b = round ((n - a) * 100)
print (a, b)