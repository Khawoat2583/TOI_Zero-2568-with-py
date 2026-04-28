"""n1 = int(input())
n2 = int(input())
n3 = int(input())
numbers = [n1,n2,n3]

max_value = numbers[0]
min_value = numbers[0]

for num in numbers:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num
print(int(max_value))"""

n1 = int(input())
n2 = int(input())
n3 = int(input())
n = [n1,n2,n3]
print(int(max(n)))