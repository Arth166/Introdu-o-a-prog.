'''Escreva um programa que leia n valores, um de cada vez, e conte quantos destes valores são
negativos, escrevendo esta informação na tela.'''

n = int(input(''))
u = 0
while n != 0:
    i = int(input(''))
    if i < 0:
        u += 1
    n -= 1
print(u)