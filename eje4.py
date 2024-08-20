'''d. Dadas dos listas, lista1 y lista2, escribir un método listas_diferencia(lista1, lista2)
que tome ambas como parámetros e imprima dos listas, cada una con:
i. Los elementos en común, en orden inverso.
ii. Los elementos no comunes, en orden alfabético.
El programa debería arrojar el siguiente resultado:
listas(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])
['c', 'b']
['a', 'e', 'd']'''
lista1=['a','b','c','u','i']
lista2=['e','b','d','c','i','t']
def buscar(lista,buscado):
    fin =True
    for letra in lista:
        if letra == buscado:
            fin=False
            break
    if fin==True:
        return True
    else:
        return False

def lista_diferencia(lista1,lista2):
    aux=[]
    for letra in lista1:
        for letra2 in lista2:
            if letra ==letra2:
                aux.append(letra)
    print(aux[::-1])
    aux1=[]
    for letra in lista1:
        if buscar(lista2,letra):
            aux1.append(letra)
    for letra in lista2:
        if buscar(lista1,letra):
            aux1.append(letra)
    aux1.sort()
    print(aux1)



lista_diferencia(lista1,lista2)