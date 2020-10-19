fin = open ("input.txt", mode = "r")
fout = open ("output.txt", mode = "w")
s = 0
while 1 > 0:
    A = fin.readline()
    if A == "":
        break
    s = (sum(list(map(int, A.split()))))
    print (s, file=fout)
    s = 0
fout.close()
fin.close()
