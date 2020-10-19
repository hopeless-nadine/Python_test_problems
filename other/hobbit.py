s = input ()
a = s.find ("h")
b = s.rfind ("h")
s = s[:b] + s[a + 1 :]
print (s)