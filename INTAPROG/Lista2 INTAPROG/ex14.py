"""Escreva um programa que dada a idade de uma pessoa, determine sua classificação segundo 
a seguinte tabela
0 – 18 Menor de idade
19 – 64 Maior de idade
65 em diante Idosa"""

ida = int(input("Qual é a sua idade? "))
if ida <= 18:
    print("Menor de idade.")
elif ida >= 19 and ida < 65:
    print("maior de idade.")
elif ida < 0:
    print("voce tem idade negativa animal?")
else: 
    print("Idosa.")