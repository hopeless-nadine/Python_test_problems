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

def readline():
    A = float(input())
    B = float(input())
    C = float(input())
    PQ = TLine(A, B, C)
    return PQ
    
def points_to_line(P, Q):
    A = P.y - Q.y
    B = Q.x - P.x
    C = - A * P.x - B * P.y
    return TLine(A, B, C)
        
def pologenie (P, Q, MN):
    if ((MN.A * P.x + MN.B * P.y + MN.C) * (MN.A * Q.x + MN.B * Q.y + MN.C)) > 0:
        return "YES"
    else:
        return "NO"
    
P = readpoint()
Q = readpoint()
AB = readline()
print (pologenie (P, Q, AB))