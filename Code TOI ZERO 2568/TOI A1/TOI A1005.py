m = int(input())
d = int(input())
mcal = m%3
st = ("")
if m>=1 and m<=3 and mcal>=1 and d <21 :
    st = ("winter")
elif m>=1 and m<=3 and mcal==0 and d >= 21 :
    st = ("spring")
elif m>=4 and m<=6 and mcal>=1 :
    st = ("spring")
elif m>=4 and m<=6 and mcal==0 and d >= 21 :
    st = ("summer")
elif m>=7 and m<=9 and mcal>=1 :
    st = ("summer")
elif m>=7 and m<=9 and mcal==0 and d >= 21 :
    st = ("fall")
elif m>=10 and m<=12 and mcal>=1 :
    st = ("fall")
elif m>=10 and m<=12 and mcal==0 and d >= 21 :
    st = ("winter")
print(st)