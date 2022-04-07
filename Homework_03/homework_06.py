klass_1 = int(input('Введите кол-во учеников в классе 1: '))
klass_2 = int(input('Введите кол-во учеников в классе 2: '))
klass_3 = int(input('Введите кол-во учеников в классе 3: '))
summ = klass_1 + klass_2 + klass_3
tables = summ // 2
add_tables = summ % 2
print('Нужно купить', tables + add_tables, 'парт')
