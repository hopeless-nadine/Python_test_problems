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

def pointperes (PQ, MN):
    x = (MN.C * PQ.B - MN.B * PQ.C) / (PQ.A * MN.B - PQ.B * MN.A)
    y = (MN.C * PQ.A - MN.A * PQ.C) / (PQ.B * MN.A - PQ.A * MN.B)
    A = TPoint(x,y)
    return A    

def pointdelitotr (A, B, k):
    x = (A.x + B.x * k) / (1 + k)
    y = (A.y + B.y * k) / (1 + k)  
    M = TPoint(x,y)
    return M

def pointperesbis (A, B, C):
    b = lenotr (A, C) 
    a = lenotr (B, C)
    k = b / a
    L1 = pointdelitotr (A, B, k)
    CL1 = points_to_line(C, L1)
    c = lenotr (A, B) 
    a = lenotr (B, C)
    k = c / a
    L2 = pointdelitotr (A, C, k)
    BL2 = points_to_line(B, L2)
    L = pointperes (CL1, BL2)
    return L

def perpen (PQ, M):
    A = -PQ.B
    B = PQ.A
    C =  PQ.B * M.x - PQ.A * M.y
    MN = TLine(A, B, C)
    return MN

def lenotr (A, B):
    l = ((A.x - B.x)**2 + (A.y - B.y)**2) ** 0.5
    return l

def rasstdopr (M, PQ):
    MN = perpen (PQ, M)
    N = pointperes (PQ, MN)
    x = lenotr (M, N)
    return x

def centrvpis (A, B, C):
    L = pointperesbis (A, B, C)
    AB = points_to_line(A, B)
    R = rasstdopr (L, AB)
    Okr = TCircle (L.x, L.y, R)
    return Okr
    

A = readpoint()
B = readpoint()
C = readpoint()
W = centrvpis (A, B, C)
print (W.x, W.y, W.R)