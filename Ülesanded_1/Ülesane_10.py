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
    print('Ответ: ', answer)
else:
    print('Читайте внимательнее!!!')

# Diagrams  https://lucid.app/lucidchart/03ef5c02-2668-4f4d-8444-fd16ca66255f/edit?viewport_loc=35%2C-196%2C3796%2C1792%2C0_0&invitationId=inv_30dd24dd-abdb-42d4-b4dc-4de7b3637356

