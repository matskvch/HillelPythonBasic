num = int(input('Введите число: '))
i = 2
count = 0       # Счетчик
while i <= num:
    count += 1
    i = i * 2
print('Показатель степени:', count, '\b, Степень:', i // 2)
