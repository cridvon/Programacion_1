# Enunciado:
# 1. Crear una función esMayorDeEdad(edad) que devuelva true si la edad es mayor o igual
# a 18, y false en caso contrario.
# 2. Crear otra función mensajeBienvenida(nombre, edad) que utilice esMayorDeEdad para
# mostrar un mensaje:
# o Si es mayor de edad: "Bienvenido/a, [nombre]!".
# o Si es menor: "Lo siento, [nombre], debes ser mayor de edad para ingresar.".

# Objetivo: Composición de funciones + condicionales.


def esMayorDeEdad(edad):
    if edad >= 18:
        return True
    else:
        return False
    
def mensajeBienvenida(nombre, edad):
    if esMayorDeEdad(edad):
        print(f"Bienvenido/a, {nombre}!")
    else:
        print(f"Lo siento, {nombre}, debes ser mayor de edad para ingresar.")

# Ejecución de la función
nombre = input("Ingrese su nombre: ")       
edad = int(input("Ingrese su edad: "))
mensajeBienvenida(nombre, edad)
