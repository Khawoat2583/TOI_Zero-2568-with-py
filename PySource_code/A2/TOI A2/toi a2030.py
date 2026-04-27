n = 5
l = []
i = 0
r = 0
s1 = []
s2 = []
s3 = []
s4 = []
s5 = []
s = [s1,s2,s3,s4,s5]
for i in range(n):
    a = list(input().split())
    l.append(a)
print(l)
i = 0
for i in range(n):
    r += 1
    s[r-1] =(l[r-1])
print(s[:n])
