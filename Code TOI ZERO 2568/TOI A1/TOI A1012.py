n = int(input())
c = str(input())
rn = int(str(n)[::-1])
if c == "+":
    cal = n+rn
else:
    cal = n*rn
print(n,c,rn,"=",cal)
