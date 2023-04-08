general_number = int(input("Введите трехзначное число "))
number = general_number
count = 0

while number > 0:
    count += 1
    number = number // 10

if count > 3 or count <= 2:
    print("Некорректный ввод")
else:
    number1 = general_number//100
    number2 = general_number//10%10
    number3 = general_number%10
    print(number1+number2+number3)