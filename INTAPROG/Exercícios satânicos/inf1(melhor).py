'''Escreva um programa que leia repetidamente um número inteiro V e um algarismo D, remova todas as ocorrências de D em V
e imprima o inteiro resultante, mantendo a ordem dos demais algarismos. O sinal negativo deve ser preservado quando o 
resultado for diferente de zero. Se todos os algarismos forem removidos, o resultado será 0. Zeros que ficarem à esquerda 
não devem aparecer na saída. 

Exemplos: remover 0 de 102030 produz 123; remover 5 de -45554 produz -44; remover 1 de 1002 produz 2; remover 7 de 777 produz 0.

Regras obrigatórias:
- Utilize while para percorrer os algarismos e para controlar a leitura até a sentinela.
- Manipule os algarismos exclusivamente com operações aritméticas, como divisão inteira, resto, soma e multiplicação.
- É proibido converter os números em strings para manipular seus algarismos. O uso normal de input() e print() é permitido.
- É proibido utilizar listas, tuplas, conjuntos ou dicionários para armazenar os algarismos.'''

v = int(input(''))
while v != -1:
    negativo = False
    if v < 0:
        v = -v
        negativo = True
    d = int(input(''))
    div = 1
    while v//div >= 10:
        div = div*10
    Imprimiu = False
    while div != 0:
        u = v//div
        if u != d and (u != 0 or Imprimiu):
            if negativo:
                u = -u
                negativo = False
            print(u, end='')
            Imprimiu = True
        v = v%div
        div = div//10
    if Imprimiu == False:
        print(0, end='')
    v = int(input('\n'))
print('Programa encerrado!')