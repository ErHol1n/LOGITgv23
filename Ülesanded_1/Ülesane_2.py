nimi=input('Mis on sinu nimi ')
if nimi=='Juku':
    print('Lähe kinno')
    vanus=int(input('Lui vana sa oled?'))
    if vanus<0 or vanus>150:
        vastus='Viga vanusrga'
    elif vanus<6:
        vastus='Tasuta pilet'
    elif vanus<14:
        vastus='Lastepilet'
    elif vanus<65:
        vastus='Täispilet'
    elif vanus<=150:
        vastus='Sooduspilet'
    print('On vaja Jukule osta', vastus)
else:
    print('Ma otan Juku')