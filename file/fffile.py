fin = open ("input.txt", mode = "r")
A = fin.readlines()
B = [ ]
fout = open ("output.txt", mode = "w")
for i in range (0, len (A)):
    B.append (len (A[i])) 
for l in range (0, len (A)):
    if len (A[l]) == max (B):
        print (A[l], end = "", file=fout)  
fin.close()
fout.close()
