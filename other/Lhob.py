s = input ()
a = s.find ("h")
b = s.rfind ("h")
for i in range (a + 1, b):
    if s[i] == "h":
        s = s[:i] + "H" + s[i + 1:]
print (s)