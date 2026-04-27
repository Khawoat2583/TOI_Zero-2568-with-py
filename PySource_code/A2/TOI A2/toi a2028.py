n = int(input())
c1 = input()
c2 = input()
wp = 0
for i in range(n):
    if int(c1[i]) + int(c2[i]) != 9:
        wp += 1
if wp== 0:
    print("YES")
else:
    print("NO", wp)