'''Elabore um programa que leia um número de entrada (n) que indicará a quantidade de números
a serem lidos. Em seguida, leia números (conforme o valor informado anteriormente) e imprima
o triplo de cada um.'''

n = int(input(''))
while n != 0:
    a = int(input(''))
    print(3*a)
    n -= 1