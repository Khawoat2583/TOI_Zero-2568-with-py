def imp(a, b):
    return (a == 'A' and b == 'T') or \
           (a == 'T' and b == 'A') or \
           (a == 'C' and b == 'G') or \
           (a == 'G' and b == 'C')

l = int(input())
cm1 = input().split()
cm2 = input().split()
n = int(input())

for i in range(n):
    ln, pos, ng = input().split()
    pos = int(pos)
    if ln == '1':
        cm1[pos] = ng
    else:
        cm2[pos] = ng

print(' '.join(cm1))
print(' '.join(cm2))

wp = 0
for a, b in zip(cm1, cm2):
    if not imp(a, b):
        wp += 1

print(wp)