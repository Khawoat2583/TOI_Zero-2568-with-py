b = list(input().split(' '))
t = list(input().split(' '))
kcal = 0
nb = str(b[0])
nbk = int(b[1])

nt = str(t[0])
nts = int(t[1])
ntk = int(t[2])

if nb == "H":
    kcal = kcal+(5*nbk)
elif nb == "O":
    kcal = kcal+(3*nbk)
elif nb == "J":
    kcal = kcal+(2*nbk)

if nt == "R" :
    if nts == 1 :
        kcal = kcal+(ntk*12)
    elif nts == 2 :
        kcal = kcal+(ntk*18)
    elif nts == 3 :
        kcal = kcal+(ntk*25)
elif nt == "T" :
    if nts == 1 :
        kcal = kcal+(ntk*15)
    elif nts == 2 :
        kcal = kcal+(ntk*20)
    elif nts == 3 :
        kcal = kcal+(ntk*30)
elif nt == "M" :
    if nts == 1 :
        kcal = kcal+(ntk*10)
    elif nts == 2 :
        kcal = kcal+(ntk*15)
    elif nts == 3 :
        kcal = kcal+(ntk*20)
print(kcal)