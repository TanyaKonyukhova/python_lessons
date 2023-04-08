general_number = int(input('Введите шестизначное число '))
number = general_number
count = 0

while number > 0:
    count += 1
    number = number // 10

if count == 6:
    n1= general_number//100000
    n2= general_number//10000%10
    n3= general_number//1000%10
    n4= general_number//10%100//10
    n5= general_number//10%10
    n6= general_number%10
    if n1+n2+n3==n4+n5+n6:
        print("Счастливый билет :)")
    else:
        print("Несчастливый билет :(")
else:

    print("Некорректный ввод")