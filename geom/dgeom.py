def distanceroot(x1, y1, x2, y2):
   s =  (x1 - x2)**2 + (y1-y2)**2
   return s
def meadiana (xa, ya, xb, yb, xc, yc):
   c = distanceroot (xa, ya, xb, yb)
   b = distanceroot (xa, ya, xc, yc)
   a = distanceroot (xb, yb, xc, yc)
   m = ((2 * c + 2 * b - a) / 4) ** 0.5
   return m
print (meadiana (float(input()), float(input()), float(input()), float(input()), float(input()), float(input())))
       