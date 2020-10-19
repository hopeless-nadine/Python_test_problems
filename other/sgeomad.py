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
        
def pologenietochnoe (P, MN):
    if MN.A * P.x + MN.B * P.y + MN.C > 0:
        return 1
    elif MN.A * P.x + MN.B * P.y + MN.C < 0:
        return 2
    else:
        return 0
    
def naodnoistorone (P, AB, MN):
    if pologenietochnoe (P, MN) == pologenietochnoe (P, AB):
        return True
    else:
        return False

def mnogougread (n):
    k = []
    for i in range (n):
        k.append (readpoint())
    return k

def prinmnogoug (k, Z):
    A = k[0]
    B = k[1]
    for i in range ( n - 2):
        C = k[i + 2]
        AB = points_to_line(A, B)
        BC = points_to_line(B, C)
        if (Z, AB, BC):
            k = k
        else:
            return "NO"
        A = B
        B = C
    C = k[0]
    AB = points_to_line(A, B)
    BC = points_to_line(B, C) 
    if (Z, AB, BC):
        return "YES" 
    else:
        return "NO"
    
n = int(input())
k = mnogougread (n)
Z = readpoint()
print (prinmnogoug (k, Z))

        