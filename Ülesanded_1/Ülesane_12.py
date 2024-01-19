price = float(input("Введите цену товара в евро: "))
discount = 0
if price == 10:
    discount = 0.1
elif price > 10:
    discount = 0.2
final_price = price - (price * discount)
print('Окончательная цена товара: ', final_price, 'евро')
