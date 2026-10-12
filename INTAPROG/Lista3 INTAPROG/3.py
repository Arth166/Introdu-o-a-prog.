'''Faça um programa que leia um valor indicando a quantidade de valores a ler em seguida. Um
número deve ser lido por vez e seu programa deve classificá-lo como positivo ou negativo.'''

n = int(input(''))
while n != 0:
    i = int(input(''))
    if i >= 0:
        print('Positivo.')
    else: 
        print('Negativo.')
    n -= 1