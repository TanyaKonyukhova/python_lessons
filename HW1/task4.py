n = int(input('Введите n '))
m = int(input('Введите m '))
number = int(input('Введите количество долек '))

if (number%n == 0 or number%m == 0) and number < n*m:
    print('Можно')
else: 
    print('Нельзя')
