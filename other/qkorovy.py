a = int (input ())
if a % 10 == 1 and not (a == 11):
    print (a, "korova", sep = " ")
elif a % 10 > 4 or a % 10 == 0 or a == 11 or a == 12 or a == 13 or a == 14:
    print (a, "korov", sep = " ")
else:
    print (a, "korovy", sep = " ")

