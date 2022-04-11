num = int(input('Введите число: '))
i = 2
count = 0       # Счетчик
if num <= 0:
    num = int(input('Натуральное число должно быть больше нуля. Введите число ещё раз: '))
else:
    while i <= num:
        count += 1
        i = i * 2
print('Показатель степени:', count, '\b, Степень:', i // 2)
