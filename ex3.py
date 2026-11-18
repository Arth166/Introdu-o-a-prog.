#Faça um algoritmo em Python mostre na tela os 30 primeiros números da sequência de Fibonacci
 
k = 0
w = 1
ve = 1
print(f"{k} {w}", end=" ")
while ve <= 28:
    i = k + w
    print(f"{i}", end=" ")
    k = w
    w = i
    ve +=1