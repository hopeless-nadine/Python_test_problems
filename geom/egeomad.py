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

def parallel (AB, R):
    D = R * (AB.A ** 2 + AB.B ** 2) ** 0.5 + AB.C
    PQ = TLine (AB.A, AB.B, D)
    return PQ

def readline():
    A = float(input())
    B = float(input())
    C = float(input())
    PQ = TLine(A, B, C)
    return PQ

AB = readline()
R = float (input())
PQ = parallel (AB, R)
print (PQ.A, PQ.B, PQ.C)


