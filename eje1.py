'''Escribir una función de nombre palabra_no_tiene_letras(palabra,
letras_prohibidas), la cual retorne True si es que los caracteres que componen
una palabra no se encuentran en una lista de caracteres prohibidos'''
def palabra_no_tiene_letras(palabra,letras_probidas):
    condicion=0
    for letra in palabra:
       for letras2 in letras_probidas:
        if letra==letras2:
           condicion+=1
    if condicion!=0:
        return False
    else:
        return True

palabra=input("Ingrese la palabra:").lower()
letras_proibida=input("Ingrese la letra proivida:").lower()
ops=palabra_no_tiene_letras(palabra,letras_proibida)
print(ops)