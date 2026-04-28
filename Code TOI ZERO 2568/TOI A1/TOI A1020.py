n1 = int(input())
n2 = int(input())
n3 = int(input())
c1 = n1>n2 and n1>n3 and n2>n3 
c2 = n1<n2 and n1<n3 and n2<n3
if c2 :
    st = "increasing"
elif c1 :
    st = "decreasing"
else:
    st = "neither"
print(st)