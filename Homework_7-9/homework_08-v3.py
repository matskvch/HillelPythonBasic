i = 2
count = 0
while True:
    num = int(input('Введите число: '))
    if num == 0:
        print('Введите число отличное от нуля')
        break
    while i <= num:
        count += 1
        i = i * 2
    print('Показатель степени:', count, '\b, Степень:', i // 2)
    break
