# Ejercicio 1: Análisis de lista de edades 
# Enunciado:
# Crea un programa que reciba una lista de edades de personas y que haga lo siguiente:

# Recorrer la lista usando un for.
# Contar cuántas personas son:

# Menores de edad (< 18)
# Adultos (18 a 59)
# Mayores (60 o más)
# Mostrar cuántas hay en cada categoría.

menor, adulto, mayor = 0, 0, 0

for i in range(1, 11):
    edad = int(input(f"Ingrese la edad de la persona {i}: "))
    if edad < 18:
        menor += 1
    elif edad >= 18 and edad <= 59:
        adulto += 1
    else:
        mayor += 1

print(f"Total de menores de edad: {menor}")
print(f"Total de adultos: {adulto}")
print(f"Total de mayores: {mayor}")



