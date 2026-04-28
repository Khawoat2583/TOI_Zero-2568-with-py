n = list(map(int,input().split(' ')))
ans = []
for i in n:
    if not i in ans:
        ans.append(i)
print(' '.join(map(str,ans)))