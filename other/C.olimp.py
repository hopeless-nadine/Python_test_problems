input = open(file = 'input.txt', mode = 'r')
output = open(file = 'output.txt', mode = 'w')
N = int (input.readline())
spisok = input.readline().split()
for i in range (0, N):
    spisok[i] = int (spisok[i]) 
kol = 1
elem = 1
kols = []
shug= []
elements = []
b = spisok[1] - spisok[0]
for i in range (0, N - 1):
    if spisok[i + 1] - spisok[i] == b:
        kol = kol + 1
    else: 
        elements.append (elem)
        kols.append (kol)
        shug.append (b)
        b = spisok[i + 1] - spisok[i]
        kol = 1
        elem = i + 1
elements.append (elem)
kols.append (kol + 1)
shug.append (b)
kol = max (kols)
c = []
for j in range (0, len (kols)):
    if kols[j] == kol:
        c.append (shug [j])
b = max (c)
elem = elements [shug.index(b)]
A = str (elem) + " " + str (kol)
output.write(A)
input.close()
output.close()