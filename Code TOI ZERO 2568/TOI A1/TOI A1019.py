n1 = int(input())
n2 = int(input())
n3 = int(input())
c1 = n1==n2 and n1==n3 and n2==n3 
c2 = n1!=n2 and n1!=n3 and n2!=n3
if c1 :
    st = "all the same"
elif c2 :
    st = "all different"
else:
    st = "neither"
print(st)