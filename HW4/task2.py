import random

n = int(input("Введите количество кустов "))
array = list()

for i in range(n):
    array.append(random.randint(0, 10))

print(*array)

array_2 = list()
for i in range(len(array) - 1):
    array_2.append(array[i-1] + array[i] + array[i+1])
array_2.append(array[-2] + array[-1] + array[0])
print(max(array_2))