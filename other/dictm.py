fin = open ("input.txt", mode = "r")
A = fin.readlines()
fin.close()
fin = open ("input.txt", mode = "r")
b = dict()
fout = open ("output.txt", mode = "w")
for i in range (len(A)):
    C = fin.readline().split()
    if C[0] in b:
        b[C[0]] = int (b[C[0]]) + int (C[1])
    else:
        b.setdefault (C[0], C[1])
for key, val in b.items():
    print(key, val)
fin.close()
fout.close()