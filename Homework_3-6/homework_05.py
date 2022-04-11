number = int(input('Введите трехзначное число: '))
part_1 = (number % 10) * 100
part_2 = ((number // 10) % 10 ) * 10
part_3 = number // 100
print('Число наобарот:', part_1 + part_2 + part_3)
