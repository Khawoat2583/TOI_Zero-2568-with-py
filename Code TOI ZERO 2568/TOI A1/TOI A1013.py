ap = str(input())
n = int(input())
if ap != "H" and n != 4567:
    s= "safe locked"
elif ap != "H" and n == 4567:
    s= "safe locked - change char"
elif ap == "H" and n != 4567:
    s= "safe locked - change digit"
else:
    s= "safe unlocked"
print(s)