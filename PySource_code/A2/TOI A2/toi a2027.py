n = int(input())
i = 0
c = 0
ns = []
for i in range(n):
    adr = int(input())
    ns.append(adr)  
fmx = max(ns)
fmxc = ns.count(fmx)
print(int(fmx))
print(int(fmxc))
