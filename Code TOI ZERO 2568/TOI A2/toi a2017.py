nd = list(map(str,input().split()))
tp = list(map(str,input().split()))
s = nd[0]
t = nd[1]
tt = tp[0]
cn = len(tp)
cal = 0
if cn == 1:
    n = 1
else:
    n = int(tp[1])
if s == "S":
    if t == "R":
        cal = cal+60
    elif t == "T":
        cal = cal+80
elif s == "M":
    if t == "R":
        cal = cal+80
    elif t == "T":
        cal = cal+100
elif s == "L":
    if t == "R":
        cal = cal+100
    elif t == "T":
        cal = cal+120
if tt == "P":
    pcal=n*15
    cal = cal+pcal
elif tt == "E":
    ecal=n*10
    cal = cal+ecal
elif tt == "N":
    cal =  cal+0
print(cal)
