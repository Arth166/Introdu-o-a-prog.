'''Escreva um programa que leia 50 valores e encontre o maior e o menor deles. Mostre o resultado.'''
'''i = 0
me = 0
ma = 0
ante = 0
foi = False
while i < 50:
    if foi:
        ante = n
    n = int(input(''))
    if n > ante and ma < n:
        ma = n
    elif ante > n and me > n:
        me = n
    i += 1
    foi = True'''

n = int(input(''))
ma = n
me = n
i = 1
while i < 50:
    n = int(input(''))
    if n > ma:
        ma = n
    elif n < me:
        me = n
    i += 1
print(f'Maior: {ma}\nMenor: {me}')