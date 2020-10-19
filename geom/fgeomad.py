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

def pointperes (PQ, MN):
    x = (MN.C * PQ.B - MN.B * PQ.C) / (PQ.A * MN.B - PQ.B * MN.A)
    y = (MN.C * PQ.A - MN.A * PQ.C) / (PQ.B * MN.A - PQ.A * MN.B)
    A = TPoint(x,y)
    return A    

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

M = readpoint()
PQ = readline()
print (rasstdopr(M, PQ))