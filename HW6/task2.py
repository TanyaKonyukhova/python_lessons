import random

min_number = int(input("Введите минимум "))
max_number = int(input("Введите максимум "))
array = []

for i in range(10):
    array.append(random.randint(-5, 10))

print(*array)

for i in range(len(array)):
    if min_number <= array[i] <= max_number:
        print(i)