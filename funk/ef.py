def distance(x1, y1, x2, y2):
   s =  ((x1 - x2)**2 + (y1-y2)**2) ** 0.5
   return s
def IsPointInCircle(x, y, xc, yc, r):
   if distance (x, y, xc, yc) <= r:
      return "YES"
   else:
      return "NO"
print (IsPointInCircle(float(input()), float(input()), float(input()), float (input()), float (input())))
