'''Desenvolva um programa que leia dois valores a e b (a<=b) e mostre os seguintes resultados:
a. Todos os números em [a,b].'''

a = int(input(''))
b = int(input(''))
j = a
if a >= b:
    print('a deve ser menor que b.')
else:
    print(f'Todos os valores no intervalo [{a},{b}]:')
    while j >= a and j <= b:
        print(j, end=' ')
        j += 1
    j = a
    print(f'\nNumeros ímpares no intervalo [{a},{b}]:')
    while j >= a and j <= b:
        if j%2 != 0:
            print(j, end=' ')
        j += 1
    j = a
    print(f'\nNumeros ímpares e múltiplos de 3 no intervalo [{a},{b}]:')
    while j >= a and j <= b:
        if j%2 != 0 and j%3 == 0:
            print(j, end=' ')
        j += 1