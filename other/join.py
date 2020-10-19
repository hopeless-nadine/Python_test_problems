a = list (map (int, input().split()))
print (' '.join (map (str, sorted (a, reverse = sum (a) % 2 == 0))))   