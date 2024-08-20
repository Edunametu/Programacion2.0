'''Escribir una función de nombre es_abc(palabra) la cual retorne True siempre y
cuando las letras que componen dicha palabra estén en orden alfabético, y False
en caso contrario'''
def es_abc(palabra):
    tam=len(palabra)
    ind=0
    salida=True
    while ind+1<tam:
        if (palabra[ind]) < (palabra[ind+1]):
            salida=True
        else:
            salida=False
            break
        ind+=1    
    if salida==True:
        return True
    else:
        return False
palabra=input("palabra:").lower()
if es_abc(palabra):
    print("la palabra esta ordenada:",palabra)
else:
    print("la palabra no esta ordenada:",palabra)