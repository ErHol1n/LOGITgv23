a = float(input('Введите число: '))
b = float(input('Введите число: '))
mt = input('Введите один из указанных символов (+, -, *, /): ')
answer = int(0)
if mt in ['+', '-', '*', '/']:
    if mt == '+':
        answer = a + b
    elif mt == '-':
        answer = a - b
    elif mt == '*':
        answer = a * b
    elif mt == '/':
        if b != 0:
            answer = a / b
        else:
            print('Ошибка: деление на ноль!')
            exit()
    print('Ответ: ', answer)
else:
    print('Читайте внимательнее!!!')
