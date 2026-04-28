n = int(input())
r = 0
while r*r < n:
    r += 1
"""
#int!!
TRUE = 1
FALSE = 0
(n % 2 != r % 2)
"""
cal = (2 * (r - 1)-(n % 2 != r % 2))
#print(r)
print(int(cal))