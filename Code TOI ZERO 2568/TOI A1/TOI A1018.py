n = int(input())
m = str("")
c = int(n)
if n >= 1 and n <= 3 :
    for i in range(n):
        n = "I"
        m =n[0]*c
elif n == 4:
    m = "IV"
elif n == 5:
    m = "V"
elif n >= 6 and n <= 8 :
    for i in range(n):
        n = "I"
        c1 = c-5
        m ="V"+n[0]*c1
elif n == 9:
    m = "IX"
elif n > 9 or n ==0:
    m = "Error : Out of range"
elif n < 0:
    m= "Error : Please input positive number"
print(m)

        