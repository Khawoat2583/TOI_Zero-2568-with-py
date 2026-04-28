def f1(s1, s2):
    if s1 == "-" and s2 == "-":
        return "-"
    elif s1 == "-" and s2 == "+":
        return "+"
    elif s1 == "-" and s2 == "x":
        return "x"
    elif s1 == "+" and s2 == "x":
        return "*"
    else:
        return "+"
n1,n2 = map(int, input().split())
g1 = [input() for _ in range(n1)]
g2 = [input() for _ in range(n1)]
go = [["-" for _ in range(n2)] for _ in range(n1)]
for i in range(n1):
    for j in range(n2):
        go[i][j] = f1(g1[i][j], g2[i][j])
for row in go:
    print(''.join(row))