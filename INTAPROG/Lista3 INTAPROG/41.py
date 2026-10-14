''' Faça um programa que leia dois valores inteiros valor inteiro x e n, calcule e mostre: somatório i = 1 de Xi até n'''

x = int(input(''))
n = int(input(''))
i = 1
s = 0
while i <= n:
    s = s + x
    i += 1
print(s)