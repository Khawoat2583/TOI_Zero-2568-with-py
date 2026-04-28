w = int(input().strip())
wl = []
t = 0
sq = 0
for i in range(w):
    x = int(input().strip())
    wl.append(x)

for i in range(w):
    if wl[i] > 18:
        sq += 1
    else:
        t += 1

if t >= sq or t == sq - 1:
    print(w)
else:
    print(sq + sq-1)