p1 = str(input())
p2 = str(input())
if len(p1) < len(p2):
    p1 += p1[:len(p2)-len(p1)]
elif len(p1) > len(p2):
    p2 += p2[:len(p1)-len(p2)]
s = ""
for na,nb in zip(p1,p2):
    if na.lower() in 'love' or nb.lower() in 'love':
        s += "w"
    else:
        s += "$"
wc = s.count("w")
if wc % 2 == 1:
    maxs = 0
    cr = 0
    for ch in s:
        if ch == 'w':
            cr += 1
            maxs = max(maxs, cr)
        else:
            cr = 0
    mx = int(maxs)
    s += str(mx)
elif "ww" not in s :
    s += '#'
sc = list(map(str,s.split("$")))
print(str(s))
