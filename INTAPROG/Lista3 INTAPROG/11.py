'''Faca um algoritmo que apresente na tela a tabela de conversão de graus Celsius para Fahrenheit
no intervalo de -100 oC a 100 oC com valores igualmente espaçados (5oC em 5oC).
Obs.: Farenheit = (9/5)*(Celsius) + 32.'''

c = -100
while c <= 100:
    f = (9/5)*c + 32
    print(f'Número em Ceucius: {c}\nNúmero em Farenheit: {f}.')
    c += 5