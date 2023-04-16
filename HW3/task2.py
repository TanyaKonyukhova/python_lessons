import random

n = int(input("Введите количество элементов в массиве "))
x = int(input("Введите x "))
array = []
index = 0

for i in range(n):
    array.append(random.randint(-5, 5))

print(*array)

min = x - array[0]

for i in range(1, n):
    count = x - array[i]
    if count < min:
        min = count
        index = i

print(f'Число {x} наиболее близко к числу {array[index]}')