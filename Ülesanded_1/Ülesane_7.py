pikk=int(input('Какого ты роста? '))
gender=str(input('Какого ты пола девушка или парень? '))
if pikk<=int(155):
    print('Ты маленького роста',pikk,'и ', gender)
elif pikk<=int(170):
    print('Ты среднего  роста',pikk,'и ', gender)
elif pikk<=int(250):
    print('Ты высокого  роста',pikk,'и ', gender)