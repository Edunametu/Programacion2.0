'''f. Un portal web requiere un formulario de alta de usuario donde se ingrese,
mínimamente, un usuario y su correspondiente contraseña. Escriba, en Python,
una función contrasena_valida(contrasena) que devuelva True en caso de
superar las siguientes validaciones sobre la contraseña proporcionada por el
usuario:
i. Longitud entre 6 y 20 caracteres.
ii. Debe contener al menos un número.
iii. Debe contener al menos dos mayúsculas.
iv. Debe contener al menos un carácter especial.
v. No puede contener espacios.
La salida esperada es la siguiente:
abc.123 es válida: False
Abc.123 es válida: False
AbC.123 es válida: True
AbC.1 23 es válida: False
ÁbC.123 es válida: False'''

#La función any() es una función incorporada de Python que se utiliza para verificar si al menos un elemento de una secuencia (como una lista, tupla o conjunto) es evaluado como verdadero
import re
#caracter_especial=re.compile(r"|,@#$%^&*()_+-=[]{}|;':./<>?")
def contraseña_valida(contraceña):
    tam=len(contraceña)
    if not (tam>6) & (tam<20):#comparar longitud
        return False
    elif not any(chr.isdigit() for chr in contraceña):#buscar numeros
        return False
    elif not any(ind.isupper()for ind in contraceña):#buscar mayusculas
        return False
    elif not " " in contraceña:
        return False
    elif not tiene_caracter_especial(contraceña):
        return False
    else:
        print("Contraseña Valida")
        return True
def tiene_caracter_especial(cadena):
    patron = re.compile(r'[^a-zA-Z0-9]')
    if patron.search(cadena):
        return True
    else:
        return False
valido=["a","b","c",1,2,3]  
valido1="abc.123"
valido2="aBc#$#123"
#cumple=contraseña_valida(valido2)
#print(cumple)
print(tiene_caracter_especial(valido2))