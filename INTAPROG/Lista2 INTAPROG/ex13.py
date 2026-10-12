"""Faça um programa que leia a data de nascimento (valores dd, mm e aaaa) 
de uma pessoa e o dia atual. Calcule e mostre a idade da pessoa em dias,
meses e anos. Verifique e mostre, também, se ela já tem idade suficiente 
para tirar carteira de habilitação e votar.

Obs.: Ignore os anos bissextos, ou seja, 1 ano equivale a 12 meses que equivale a 365 dias."""

diaani = int(input("Digite o dia do seu niver: "))
mesani = int(input("Digite o mes do seu niver: "))
anoani = int(input("Digite o ano do seu ani: "))
diaatu = int(input("Digite o dia atual: "))
mesatu = int(input("Digite o mes atual: "))
anoatu = int(input("Digite o ano atual: "))
datanasc = anoani*365+mesani*30+diaani
dataatua = anoatu*365+mesatu*30+diaatu
#idades
idadedias = dataatua - datanasc
idadeano = idadedias//365
idademes = (idadedias%365)/30

print(f"A sua idade em dias é {idadedias}, em meses é {idademes} e a sua idade é {idadeano}.")