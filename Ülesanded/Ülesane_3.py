from random import *
#Pinginaabrid
#'A', 'B'
n1=input('Esimene nimi ')
n2=input('Teine nimi')
if n1.upper()=='A' and n2.upper()=='B'or n1.upper()=='B' and n2.upper()=='A':
    print('Pinginaabrid')
else:
    print('Nad ei ole naabrid')
if n1.upper() in ['A','B'] and n2.upper() in ['A', 'B']:
    print('Pinginaabrid')
else:
    print('Nad ei ole naabrid')