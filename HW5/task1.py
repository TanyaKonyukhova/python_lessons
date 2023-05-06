num_1 = int(input("Введите первое число "))
num_2 = int(input("Введите второе число "))

def degree(num_1, num_2):
    if num_2 == 0:
        return 1
    else:
        return num_1 * degree(num_1, num_2 - 1)
        
        
if num_1 < 0 or num_2 < 0:
    print("Некорректные значения")
else:
    print(degree(num_1, num_2))