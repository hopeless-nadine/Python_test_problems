a = {"a" : 1, "b" : 2, "c" : 3}
print (a.items())
print (a.keys())
for key in a.keys():
    print (a[key])
for key, value in a.items():
    print (key,value,sep=" ")