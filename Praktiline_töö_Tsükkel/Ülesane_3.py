import random
k=0
while True:
    k+=1
    print(k, 'ülesane')
    a= random.randint(1,50)
    b = random.randint(1, 50)
    p=5
    while True:
        v=int(input(f'{a}+{b}='))
        p-=1
        if v==a+b:
            print('Õige vastus!')
            break
        elif p==0:
            print('a+b=a+b')
            break