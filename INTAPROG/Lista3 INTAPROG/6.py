'''Escreva um programa que calcule a média dos números digitados pelo usuário se eles forem pares.
Termine a leitura se o usuário digitar 0.'''

n = int(input(''))
s = 0
i = 0
somou = False
while n != 0:
    if n%2 == 0:
        s = s + n
        i += 1
        somou = True
    n = int(input(''))
if somou:
    print(s/i)
else:
    print('não há pares.')