"""Escreva um programa que leia três valores a, b e c, e posteriormente calcula e escreve a média
ponderada com peso 5,0 para o maior dos três valores e peso 2,5 para os outros dois."""
a = int(input("Escolha um número inteiro: "))
b = int(input("Escolha outro número inteiro: "))
c = int(input("Escolha mais um número inteiro: "))
if a >= b and a >= c:
    med = (a*5+b*2.5+c*2.5)/10
elif b>=c and b>=a:
    med = (a*2.5+b*5+c*2.5)/10
else:
    med = (a*2.5+b*2.5+c*5)/10
print(f"A média é {med}.")