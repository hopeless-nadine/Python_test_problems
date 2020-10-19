n = int (input())
for i in range (100, 1000):
    a = i // 100
    b = (i % 100)//10
    c = i % 10
    if a + b + c == n: 
        print (i)
    