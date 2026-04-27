l1 = input().split()
l2 = input().split()

if l1 == l2:
    s =1000000
elif l2[1] == l1[1] and l2[0] != l1[0]:
    s =100000
elif l2[1][2:] == l1[1][2:] and l2[0] == l1[0]:
    s=2000
elif l2[1][3:] == l1[1][3:] and l2[0] == l1[0]:
    s=1000
elif l2[1][2:] == l1[1][2:] and l2[0] != l1[0]:
    s=200
elif l2[1][3:] == l1[1][3:] and l2[0] != l1[0]:
    s=100
elif l2[1] != l1[1] and l2[0] == l1[0]:
    s=20
else:
    s=0
print(s)

"""#1
n = input().split()
a = str(n[0])
b = str(n[1])
bz = int(n[1])
bc = (" ".join(b))
s = list(map(int,bc.split())) 
sc = len(s)
print(a)
print(b)
print(bc)
print(s)
print(sc)
#2
n1 = input().split()
a1 = str(n1[0])
b1 = str(n1[1])
b1z = int(n1[1])
bc1 = (" ".join(b1))
s1 = list(map(int,bc1.split()))
s1c = len(s1)
print(a1)
print(b1)
print(bc1)
print(s1)
print(s1c)
#index = 0 1 2 3 4 ...
#n     = 1 2 3 4 5 ...
if sc == 5 and s1c == 5 and bz >=0 and b1z >= 0:
    if a == a1 and s == s1:
        st =(10**6)
    elif a != a1 and s == s1:
        st =(10**5)
    elif a == a1 and s[3] == s1[3] and s[4] == s1[4]:
        st =(10**3)
    elif a == a1 and s[2] == s1[2] and s[3] == s1[3] and s[4] == s1[4]:
        st =(2000)
    elif a != a1 and s[3] == s1[3] and s[4] == s1[4]:
        st =(10**2)
    elif a != a1 and s[2] == s1[2] and s[3] == s1[3] and s[4] == s1[4]:
        st =(200)
    elif a == a1 and s != s1:
        st =(20)    
    else:
        st =(0)
else:
        st =(0)
print(st) """