def bubble(array):
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] < array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff
 
N = int (input())
a = input().split()
bubble(a)
for i in range (0, N):
    print (a[i], " ", sep ="", end ="")