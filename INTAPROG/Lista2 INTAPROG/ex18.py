'''Um usuário deseja um programa onde possa escolher que tipo de média deseja calcular a partir de
três notas. Faça um programa que leia as notas, a opção (caractere – tipo char) escolhida pelo
usuário e calcule a média:
• ‘a’ - Aritmética.
• ‘p’ - Ponderada (pesos: 3,3,4).'''

num1 = int(input('Escolha um numero: '))
num2 = int(input('Escolha outro numero: '))
num3 = int(input('Escolha mais um numero: '))
tipo = input('Escolha um tipo de operação:\na = Aritmética\np = Ponderada\n ')

if tipo == "a":
    med = (num1+num2+num3)/3
    print(f'{med: .2f}')
elif tipo == "p":
    med = (num1*3+num2*3+num3*4)/10
    print(f'{med: .2f}')
else:
    print('Coloque um tipo válido.')