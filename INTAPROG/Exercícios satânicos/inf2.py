'''Escreva um programa que leia repetidamente números inteiros e compacte cada sequência de algarismos consecutivos iguais, mantendo apenas um algarismo de cada sequência.

A ordem dos algarismos deve ser preservada. Algarismos iguais separados por um algarismo diferente não devem ser eliminados. O sinal negativo deve ser preservado, e a entrada 0 deve produzir 0.

Exemplos: 112233 produz 123; -45554 produz -454; 100002200 produz 1020; 101010 permanece 101010.
'''

v = int(input(''))
while v != -1:
    div = 1
    negativo = False
    if v < 0:
        negativo = True
        v = -v
    while v//div >= 10:
        div = div*10
    k = 0
    z = 0
    repetiu = False
    imprimiu = False
    while div > 0:
        u = v//div
        if repetiu:
            z = k
        k = u
        if z != k:
            if negativo:
                print('-', end='')
                negativo = False
            print(k, end='')
            imprimiu = True
        v = v%div
        div=div//10
        if imprimiu == False:
            print(0)
        repetiu = True
    v = int(input('\n'))
print('Programa encerrado!')