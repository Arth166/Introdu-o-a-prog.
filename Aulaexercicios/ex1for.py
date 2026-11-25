def implis(lista):
    print(lista)
def crialist2(list1, list2):
    for i in range(len(list1)):
        if i%2 == 0:
            list2.append(list1[i]*5)
        else:
            list2.append(list1[i]+5)
    return list2
def lelist1(lista1):
    lista1  = []
    for i in range(10):
        a = int(input(''))
        lista1.append(a)
    return lista1
def main():
    lista1 = []
    lista2 = []
    lista1 = lelist1(lista1)
    lista2 = crialist2(lista1, lista2)
    implis(lista1)
    implis(lista2)
main()