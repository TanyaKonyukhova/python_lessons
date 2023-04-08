number = int(input("Введите количество журавликов "))
person1 = 0
other = 0

if number%4==0:
    person1 = int(number/2)
    other = int(person1/2)
    print(f"Катя сделала {person1} журавликов, а мальчики сделали по {other}")
else:
    print("Некорректное значение журавликов :(")
