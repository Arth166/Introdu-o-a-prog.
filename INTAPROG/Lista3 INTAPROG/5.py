'''Faça um programa que calcule a média aritmética de vários valores inteiros positivos, inseridos
pelo usuário. O final da leitura acontecerá quando for lido um valor negativo.'''

n = int(input(''))
s = 0
i = 0
while n >= 0:
    s = s + n
    i += 1
    n = int(input(''))
if i > 0:
    print(s/(i))
else: 
    print('Sem numeros positivos.')