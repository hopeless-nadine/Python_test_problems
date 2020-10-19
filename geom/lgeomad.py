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

class TCircle:
    def __init__(self, x, y, R):
        self.x = x
        self.y = y
        self.R = R   

def lenotr (A, B):
    l = ((A.x - B.x)**2 + (A.y - B.y)**2) ** 0.5
    return l
        
def rasstdopr (M, PQ):
    MN = perpen (PQ, M)
    N = pointperes (PQ, MN)
    x = lenotr (M, N)
    return x

def seredinaotr (A, B):
    x = (B.x + A.x) / 2
    y = (B.y + A.y) / 2  
    M1 = TPoint(x,y)
    return M1

        
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

def perpen (PQ, M):
    A = -PQ.B
    B = PQ.A
    C =  PQ.B * M.x - PQ.A * M.y
    MN = TLine(A, B, C)
    return MN

def pointperes (PQ, MN):
    x = (MN.C * PQ.B - MN.B * PQ.C) / (PQ.A * MN.B - PQ.B * MN.A)
    y = (MN.C * PQ.A - MN.A * PQ.C) / (PQ.B * MN.A - PQ.A * MN.B)
    A = TPoint(x,y)
    return A    

def pointperesserper (A, B, C):
    M1 = seredinaotr (A, B)
    AB = points_to_line(A, B)
    H1M1 = perpen (AB, M1)
    M2 = seredinaotr (A, C)
    AC = points_to_line(A, C)
    H2M2 = perpen (AC, M2)
    O = pointperes (H1M1, H2M2)
    return O

def centropis (A, B, C):
    O = pointperesserper (A, B, C)
    AB = points_to_line(A, B)
    R =  lenotr (O, A)
    Okr = TCircle (O.x, O.y, R)  
    return Okr

A = readpoint()
B = readpoint()
C = readpoint()
W = centropis (A, B, C)
print (W.x, W.y, W.R)    
    