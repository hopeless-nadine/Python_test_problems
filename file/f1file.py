fin = open ("input.txt", mode = "r")
A = fin.readlines()
k = 0
fout = open ("output.txt", mode = "w")
for i in range (0, len (A)):
    if len (A[i]) >= k:
        k = len (A[i])
for l in range (0, len (A)):
    if len (A[l]) == k:
        print (A[l], end ="", file=fout)  
fin.close()
fout.close()