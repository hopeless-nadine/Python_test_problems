import math

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

N = int (input())
A = readpoint()
C = A
Z = A
S = 0
for i in range (1, N):
    B = readpoint()
    S = S + C.x * B.y - B.x * C.y
    C = B
S = S + B.x * Z.y - Z.x * B.y
S = math.fabs (S/2)
print (S)