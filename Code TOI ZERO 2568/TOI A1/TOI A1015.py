n = str(input())
s = str(input())
a = int(input())
ac= str(a)
nc = len(n)
sc = len(s)
if nc > 5 and sc > 5:
    p = n[0]+n[1]+s[-1]+ac[-1]
else:
    p = n[0]+ac+s[-1]
print(p)