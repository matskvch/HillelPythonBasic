while True:
    num = int(input('Введите натуральное число: '))
    if num <= 0:
        print('Натуральное число должно быть больше нуля')
        break
    for i in range(1, num + 1):
        if i ** 2 <= num:
            print(i ** 2)
    break
