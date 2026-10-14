'''Escreva um programa que leia um valor e informe seus divisores em caso de não ser primo, ou
mostre na tela “É PRIMO” caso contrário.'''

v = int(input(''))
primo = True
if v <= 1:
    primo = False
i = 0
div = 2
while i<v:
    if v%div == 0:
        if div != v:
            print(div)
            primo = False
    div += 1
    i += 1
if primo:
    print('É PRIMO')