class TPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return str(self.x) + " " + str(self.y)
        

class TLine:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        
def readpoint():
    x = float(input())
    y = float(input())
    A = TPoint(x,y)
    return A
    
def points_to_line(P, Q):
    A = P.y - Q.y
    B = Q.x - P.x
    C = - A * P.x - B * P.y
    return TLine(A, B, C)
        

A = readpoint()
B = readpoint()
AB = points_to_line(A, B)
print (AB.A, AB.B, AB.C)
