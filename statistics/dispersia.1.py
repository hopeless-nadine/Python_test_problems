s = (list (map(int, input().split())))
n = len (s)
sum = sum (s)
middle = sum/n
sum_sq = 0
for i in range (n):
    sum_sq = sum_sq + (middle - s[i]) ** 2
SD = (sum_sq/(n-1)) ** 0.5
print (SD)