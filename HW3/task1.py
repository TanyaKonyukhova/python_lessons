import random

n = int(input("Введите количество элементов в массиве "))
x = int(input("Введите искомое число "))
array = []
count = 0

for i in range(n):
    array.append(random.randint(-5, 5))

print(*array)

for i in array:
    if x == array[i]:
        count += 1 

if count == 0:
    print("Число в массиве не встречается")
else:
    print(f"Число встречается {count} раз")