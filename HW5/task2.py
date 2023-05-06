num_1 = int(input("Введите первое число "))
num_2 = int(input("Введите второе число "))

def sum_num(num_1, num_2):
    if num_1 == 0:
        return num_2
    else:
        return sum_num(num_1 - 1, num_2 + 1)
        
        
if num_1 < 0 or num_2 < 0:
    print("Некорректные значения")
else:
    print(sum_num(num_1, num_2))