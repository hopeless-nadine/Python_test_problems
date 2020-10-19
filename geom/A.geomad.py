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

def peres (PQ, MN):
    if PQ.A * MN.C == PQ.C * MN.A and  PQ.B * MN.C == PQ.C * MN.B:
        return 2
    elif PQ.A * MN.B == PQ.B * MN.A:
        return 0
    else:
        return 1
def pointperes (PQ, MN):
    x = (MN.C * PQ.B - MN.B * PQ.C) / (PQ.A * MN.B - PQ.B * MN.A)
    y = (MN.C * PQ.A - MN.A * PQ.C) / (PQ.B * MN.A - PQ.A * MN.B)
    A = TPoint(x,y)
    return A    

A = readpoint()
B = readpoint()
AB = points_to_line(A, B)
C = readpoint()
D = readpoint()
CD = points_to_line(C, D)
print (peres (AB, CD))
if peres (AB, CD) == 1:
    K = pointperes (AB, CD)
    print (K.x, K.y)
