fin = open ("input.txt", mode = "r")
C = fin.readlines()
fout = open ("output.txt", mode = "w")
for i in range (0, len (C)):
    S = C[i]
    if not (S.find (" G") == -1) or S.find ("G") == 0:
        print(S, file=fout, end ="")
fin.close()
fout.close()