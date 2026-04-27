w = str(input())
wl = w.lower()
wc = len(wl)
s = ""
st = []
if "buu" in wl:
    s += "Yes"
    mx = 0
    cr = 0
    for ch in wl:
        if ch == 'u':
            cr += 1
            mx = max(mx, cr)
        else:
                cr = 0
    s += " "
    s += str(mx)
elif "b" in wl:
    fb = wl.find("b")
    if fb:
        s = w[:fb+1] +'U'*(len(wl)-fb- 1)
else:
    wbuu = ["B","U","U"]
    for i in range(0,wc):
       st.append(wbuu[i%3])
    s = ("".join(st))  
print(str(s))