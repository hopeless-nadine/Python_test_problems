def bubblevozr(array):
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff

def bubbleub(array):
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] < array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff
 
a = input().split()
N = len (a)
s = 0
for i in range(N):
    s = s + int (a[i])
if s % 2 == 0:
    bubblevozr(a)
else:
    bubbleub(a)
for i in range (N):
    print (a[i], " ", sep ="", end ="")
