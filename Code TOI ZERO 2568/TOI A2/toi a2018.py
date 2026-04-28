a = input().split()
a1 = str(a[0])
a2 = int(a[1])
i = 0
s = []
cal = i%3
#index   "0"     "1"    "2"
cl = ["Red","Green","Blue"]
#n   = pattern[0 1 2 3 .....]
#n%3 = pattern[0 1 2.... 0 1 2]
if a1 == "R":
    for i in range(0,a2):
        s.append(cl[i%3])
elif a1 == "G":
    for i in range(1,a2+1):
        s.append(cl[(i%3)])
elif a1 == "B":
    for i in range(2,a2+2):
        s.append(cl[(i%3)])
print(" ".join(s))