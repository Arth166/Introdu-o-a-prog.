"""Elabore um programa que dado o número do mês do ano indica quantos dias tem esse mês.
Obs.: Considere fevereiro como tendo 28 dias."""

num = int(input("Escreva o numero de um mês do ano: "))
if num == 1:
    print("Janeiro possui 31 dias.")
elif num == 2:
    print("Fevereiro possui 28 dias.")
elif num == 3:
    print("Março possui 31 dias.")
elif num == 4:
    print("Abril possui 30 dias.")
elif num == 5:
    print("Maio possui 31 dias.")
elif num == 6:
    print("Junho possui 30 dias.")
elif num == 7:
    print("Julho possui 31 dias.")
elif num == 8:
    print("Agosto possui 30 dias.")
elif num == 9:
    print("Setembro possui 31 dias.")
elif num == 10:
    print("Outubro possui 30 dias.")
elif num == 11:
    print("Novembro possui 31 dias.")
elif num > 12:
    print("Ce parece boboca.")
else: 
    print("Dezembro tem 31 dias.")