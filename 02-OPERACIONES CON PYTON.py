import os  # Importa el módulo os para poder limpiar la consola

# Practica 7: Suma, Resta, Multiplicacion, Division
print(input("------Presione Enter Para Inciar con los Programas------"))  # Solicita al usuario que presione Enter para comenzar
print("\nPractica 7")
# Realiza operaciones aritméticas básicas
suma = 20 + 23 + 44  # Suma de tres valores
resta = 23 - 20 - 90  # Resta de tres valores
multiplicacion = 20 * 23 * 1.8913  # Producto de tres números
division = 5000 / 230 / 2  # Cociente de tres números
# Muestra los resultados de las operaciones
print("Suma: ", suma, "\nResta: ", resta, "\nMultiplicacion: ", multiplicacion, "\nDivision: ", division)
print(input("------Presione Enter Para Pasar A La Siguiente Practica------"))  # Solicita al usuario que presione Enter para continuar
os.system("cls")  # Limpia la consola

# Practica 8: Como calcular Exponenetes en Python
print("\nPractica 8")
mil24 = 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2  # Multiplicación repetida para calcular 2 elevado a 10
print("El resultado de multiplicar 2 para obtener:", mil24)  # Muestra el resultado
print(input("------Presione Enter Para Pasar A La Siguiente Practica------"))  # Solicita al usuario que presione Enter para continuar
os.system("cls")  # Limpia la consola

# Practica 9: Los floats y el metodo round()
print("\nPractica 9")
print("Se necesita redondear el numero 17.567383292929200234, hasta que tenga 5 decimales")  # Descripción del proceso de redondeo
numeero = round(17.567383292929200234, 5)  # Redondea el número a 5 decimales
print(numeero)  # Muestra el número redondeado
print(round(17.567383292929200234, 5))  # Imprime directamente el resultado del redondeo
print(input("------Presione Enter Para Pasar A La Siguiente Practica------"))  # Solicita al usuario que presione Enter para continuar
os.system("cls")  # Limpia la consola
