import random

n = int(input("Введите количество элементов первого множества "))
x = int(input("Введите количество элементов второго множества "))
array_1 = []
array_2 = []
array_3 = []

for i in range(n):
    array_1.append(random.randint(-5, 10))

for i in range(x):
    array_2.append(random.randint(-5, 10))

print(*array_1)
print(*array_2)

for i in range(len(array_1)):
    for j in range(len(array_2)):
            if array_2[j] == array_1[i]:
                array_3.append(array_2[j])

last_array = []

for i in set(array_3):
    if array_3.count(i) > 1:
        last_array.append(i)

print(*last_array)