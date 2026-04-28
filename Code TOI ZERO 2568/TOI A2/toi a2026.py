n = int(input())
i = 0
c = 0
rl = []
for i in range(n):
    adr = input().split()
    ct = int(adr[1])
    if ct > 15:
        c += 1
    rl.append(adr)
fmax = max(rl,key=lambda x:int(x[1]))
print(c)
print(" ".join(fmax))