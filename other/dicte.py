fin = open ("input.txt", mode = "r")
A = fin.readline().split()
n = int (A[0])
m = int (A[1])
D = []
E = []
fout = open ("output.txt", mode = "w")
for i in range (0, n):
    C = fin.readline().split()
    D.append (C[0])
for l in range (0, m):
    K = fin.readline().split()
    E.append (K[0])
N = set (D)
M = set (E)
print (len (N&M), file=fout)
print (*sorted (N&M), file=fout)
print (len (N-M), file=fout)
print (*sorted (N-M), file=fout)
print (len (M-N), file=fout)
print (*sorted (M-N), file=fout)
fin.close()
fout.close()