total_people = int(input('Введите общее количество людей: '))
bus_capacity = int(input('Введите размер автобуса (количество мест): '))
buses_needed = total_people // bus_capacity
remaining_people = total_people % bus_capacity
print('Для перевозки', total_people, 'человек в автобусах размером', bus_capacity, 'мест(а) потребуется:')
print('Количество полностью заполненных автобусов:', buses_needed)
print('Количество людей в последнем автобусе:', remaining_people)
