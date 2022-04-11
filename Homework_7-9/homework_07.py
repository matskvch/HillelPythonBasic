# ДЗ 7. Последовательности целых чисел

max_num = min_num = num = int(input('Введите число: '))
summa = 0
count = 0
even = 0    # Четное
odd = 0     # Нечетное
while num != 0:
    summa += num
    count += 1
    if num > max_num:
        max_num = num
    elif num < min_num:
        min_num = num
    if num % 2 == 0:
        even += 1
    if num % 2 != 0:
        odd += 1
    num = int(input('Введите число: '))
print('Всего вы ввели', count, 'чисел')
print('Сумма чисел =', summa)
print('Среднее арифметическое всех введённых чисел =', round(summa / count, 2))
print('Максимальное число =', max_num, '\b, Минимальное число =', min_num)
print('Кол-во четных чисел:', even, '\b, Кол-во нечетных чисел:', odd)
