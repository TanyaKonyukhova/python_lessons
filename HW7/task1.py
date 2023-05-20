line = input("Введите стих ")
array = []

def checking_rhythm(poem):
    poem = poem.split()
    array = []
    for i in poem:
        sum_w = 0
        for j in i:
            if j in 'аеёиоуыэюя':
                sum_w += 1
        array.append(sum_w)
    return len(array) == array.count(array[0])


if checking_rhythm(line):
    print('Парам пам-пам')
else:
    print('Пам парам')