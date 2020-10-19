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

def perpen (PQ, M):
    A = -PQ.B
    B = PQ.A
    C =  PQ.B * M.x - PQ.A * M.y
    MN = TLine(A, B, C)
    return MN

PQ = readline()
M = readpoint()
AB = perpen (PQ, M)
print (AB.A, AB.B, AB.C)