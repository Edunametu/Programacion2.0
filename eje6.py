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
def contraseña_valida(contraceña):
    tam=len(contraceña)
    if (tam>6) & (tam<20):
        print("llego1")
        valido=False
        tiene_mayuscula=False
        for caracter in contraceña:
            if isinstance(caracter,int):
                print("llego2")
                valido=True
                break
        if valido==True:
           if tiene_mayuscula == any(c.isupper()for c in contraceña):
                print("llego3")
                return True
           else:
               print("llego")
        else:
            return False   
    else:
        return False            

valido="abc.123"  '''false'''
valido2="aBc.123"
print(contraseña_valida(valido2))