import random

total_cost = 0
print('Добро пожаловать в магазин!')

choise = input('Желаете ли вы купить молоко? (ответ: да или нет) ')
if choise == 'да':
    total = int(input('Сколько вы хотите купить? '))
    mcost = total * float(random.uniform(0.50, 2.0))
elif choise == 'да':
    total = int(input('Сколько вы хотите купить? '))
    ecost = total * float(random.uniform(1.0, 3.0))
elif choise == 'да':
    total = int(input('Сколько вы хотите купить? '))
    bcost = total * float(random.uniform(1.2, 2.5))

print('-------------------------')
if 'mcost' in locals():
    print(f'Milk Cost: {mcost}')
if 'ecost' in locals():
    print(f'Egg Cost: {ecost}')
if 'bcost' in locals():
    print(f'Bread Cost: {bcost}')


