n = int(input())
nt = list(map(int,input().split()))
num = 0
for i in range(n):
    cr = nt[i]
    if i == 0:
        l = 0
    else:
        l = nt[i-1]
    if i == n-1:
        r = 0
    else:
        r = nt[i+1]
    if cr > l and cr > r:
        num += 1
print(num)