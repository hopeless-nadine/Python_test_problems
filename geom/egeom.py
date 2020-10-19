def distanceroot(x1, y1, x2, y2):
   s =  (x1 - x2)**2 + (y1-y2)**2
   return s
def visota (xa, ya, xb, yb, xc, yc):
   c = distanceroot (xa, ya, xb, yb)
   b = distanceroot (xa, ya, xc, yc)
   a = distanceroot (xb, yb, xc, yc)
   h = (c - ((c + a - b) / (2 * (a** 0.5)))**2)  ** 0.5
   return h
print (visota (float(input()), float(input()), float(input()), float(input()), float(input()), float(input())))