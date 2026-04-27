n = int(input())
d = {} #dict
c = 0
for i in range(n):
    x = int(input())
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
#    print(d[x],end="")
#    print("------")
    c = max(c, d[x])

print(c)