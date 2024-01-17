import random

items = ['молоко', 'хлеб', 'яйца', 'сыр', 'вода']
quantities = []
total_cost = 0
print('Добро пожаловать в магазин!\n', '-------------------------------')
for item in items:
    quantity = input(f'Сколько штук {item} вы хотите купить? ')
    quantity = int(quantity)
    quantities.append(quantity)
print('\nЧек:\n', '-------------------------------')
for item, quantity in zip(items, quantities):
    price = random.uniform(5, 15)
    cost = price * quantity
    total_cost += cost
    print(f'{item}: {quantity} шт. x {price:.2f} руб. = {cost:.2f} руб.')
print('-------------------------------\n', f'Итого: {total_cost:.2f} руб.')
