import os  # Importa el módulo 'os' para interactuar con el sistema operativo, como limpiar la consola.

#Practica 2: Uso de Variables
print(input("------Presiona Enter Para Continuar-----"))  # Espera a que el usuario pulse Enter para seguir adelante.
print("Ejercicio 2")  # Presenta el título de la actividad.
message = "Aprendiendo Python en Ceti"  # Define un texto en la variable 'message'.
value1 = 25  # Asigna el valor numérico 25 a 'value1'.
value2 = 5   # Asigna el valor numérico 5 a 'value2'.
total = value1 + value2  # Calcula la suma de 'value1' y 'value2' y guarda el resultado en 'total'.
print("Este es el mensaje para quienes revisan el código:", message)  # Muestra el contenido de 'message'.
print("Valor 1:", value1)  # Muestra el valor de 'value1'.
print("Valor 2:", value2)  # Muestra el valor de 'value2'.
print("La suma total es:", total)  # Presenta el resultado de la suma de 'value1' y 'value2'.
print(input("------Presiona enter para avanzar al siguiente ejercicio-----"))  # Espera a que el usuario pulse Enter para seguir.
os.system("cls")  # Limpia la pantalla de la consola.

#Practica 3: Manipulación de Cadenas
print("\nEjercicio 3")  # Presenta el título de la actividad con un salto de línea.
mensaje1 = 'Este texto se mostró con comillas simples:'  # Define un mensaje que utiliza comillas simples en 'mensaje1'.
mensaje2 = "Y este texto usa comillas dobles:"  # Define un mensaje que utiliza comillas dobles en 'mensaje2'.
descripcion = 'Para mostrar en la consola ' \
              'utiliza la función "print()"'  # Guarda un mensaje que explica cómo utilizar 'print()'.
print(mensaje1, "''")  # Muestra 'mensaje1' seguido de un par de comillas simples.
print(mensaje2, '""')  # Muestra 'mensaje2' seguido de un par de comillas dobles.
print(descripcion)  # Imprime el contenido de la variable 'descripcion'.
print(input("------Presiona enter para pasar al siguiente ejercicio-----"))  # Espera que el usuario pulse Enter para avanzar.
os.system("cls")  # Borra la consola.

# Practica 4: Como concatenar
print("\nPractica 4")  # Muestra el título de la práctica seguido de un salto de línea.
p1 = "Ingeniero"  # Asigna el valor "Ingeniero" a la variable 'p1'.
p2 = "Mecatronico"  # Asigna el valor "Mecatronico" a la variable 'p2'.
com = p1 + " " + p2 + " "  # Concatena 'p1' y 'p2' con un espacio entre ellos y lo asigna a 'com'.
n = "Eduardo"  # Asigna el nombre "Eduardo" a la variable 'n'.
ap = "Gamez"  # Asigna el apellido "Gamez" a la variable 'ap'.
am = "Rodriguez"  # Asigna el apellido "Rodriguez" a la variable 'am'.
print(p1 + p2)  # Imprime 'p1' concatenado con 'p2' sin espacios.
print(com)  # Imprime la concatenación de 'p1' y 'p2' con un espacio entre ellos.
print(p1 + ' ' + p2)  # Corrige el comentario para reflejar la concatenación correcta de 'p1' con 'p2'.
print(n + " " + ap + " " + am + " ")  # Imprime el nombre completo concatenado.
print("Dos numeros concatenados:\n""10" + "12")  # Concatena y muestra las cadenas "10" y "12".
print(input("------Presione enter para pasar a la siguiente practica-----"))  # Espera a que el usuario presione Enter para continuar.
os.system("cls")  # Limpia la consola.


# Practica 5: Los métodos upper(), lower() y title en Python
print("\nPractica 5")  # Muestra el título de la práctica antecedido por un salto de línea.
fra1 = "enrique barros fernandez".title()  # Capitaliza la primera letra de cada palabra y lo guarda en 'fra1'.
fra2 = "Esta Es Una Frase Para Ser Formateada".lower()  # Convierte toda la cadena a minúsculas y lo asigna a 'fra2'.
fra3 = "Esta Es Una Frase Para Ser Formateada".upper()  # Convierte toda la cadena a mayúsculas y lo asigna a 'fra3'.
print(fra1)  # Muestra 'fra1' con la primera letra de cada palabra en mayúscula.
print(fra2)  # Muestra 'fra2' en minúsculas.
print(fra3)  # Muestra 'fra3' en mayúsculas.
print(input("------Presione enter para terminar-----"))  # Espera a que el usuario pulse Enter para finaliza.
os.system("cls")  # Borra el contenido de la consola.

# Practica 6: Saltos de Línea y Tabulaciones
print("\nPractica 6")  # Imprime el título de la práctica con un salto de línea.
print("-Python.\n-JavaScript.\n-Java.\n-PHP.\n-TypeScript.\n-SQL.\n-COBOL.")  # Imprime una lista de lenguajes de programación, cada uno en una nueva línea.
print(input("------Presione enter para terminar-----"))  # Espera a que el usuario presione Enter antes de terminar.
os.system("cls")  # Limpia la consola.