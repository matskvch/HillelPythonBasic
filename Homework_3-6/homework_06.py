klass_1 = int(input('Введите кол-во учеников в классе 1: '))
klass_2 = int(input('Введите кол-во учеников в классе 2: '))
klass_3 = int(input('Введите кол-во учеников в классе 3: '))
tables = klass_1 // 2 + klass_2 // 2 + klass_3 // 2 + klass_1 % 2 + klass_2 % 2 + klass_3 % 2
print('Всего учеников', klass_1 + klass_2 + klass_3)
print('Нужно купить', tables, 'парт')
