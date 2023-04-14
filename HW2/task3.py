n = int(input("Введите число "))
number = 2
degree = 0
result = 0

while 2 ** degree < n:
    result = number ** degree
    degree += 1
    print(result)