sal = int(input("Digite seu salário bruto: "))
pres = int(input("Digite o valor da prestação: "))
if pres <= 0.3*sal:
    print("Valor do empréstimo pode ser concedido.")
else: 
    print("Valor do empréstimo não pode ser concedido.")