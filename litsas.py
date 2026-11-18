
def implista(n):
    i = 0
    while i < len(n):
        print(n[i])
        i+=1


#função append:
'''n = [2, 4, 16]
n.append(7)
implista(n)'''
#função insert:
'''n = [2, 4, 16]
n.insert(1, 8)
implista(n)'''
#trocar de lugar coisas na lista:
#quero trocar a posição 3 com a 0
'''n = [2, 3, 5, 10]
temp = n[0]
n[0] = n[3]
n[3] = temp'''
#remoção de elementos de listas
'''n = [1,2,4,5,10,5,2]
n.remove(2) #remove somente a primeira ocorrencia
n.pop(5) #remove o indice 5 (segundo 5)
del n [0] #msm coisa q o pop'''

#remover todas as ocorrencias de algo:
n = [2,7,1,1,1]
i = 0
while i < len(n):
    if n[i] == 1:
        n.pop(i)
    else:
        i += 1
implista(n)