import random

n = int(input("Введите количство монеток "))
count_zero = 0
count_one = 0

for _ in range(n):
    temp = int(random.randint(0, 1))
    print(temp)
    if temp == 1:
        count_one +=1
    else:
        count_zero +=1

if count_one > count_zero:
    print(count_zero)
elif count_one < count_zero:
    print(count_one)
else:
    print("Не важно, что переворачивать")