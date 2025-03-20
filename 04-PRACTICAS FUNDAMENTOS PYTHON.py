import os  # Importa el módulo os para poder limpiar la consola

# Practica 19: Crear y Manejar Tuplas
print(input("------Presione Enter Para Iniciar------"))  # Solicita al usuario que presione Enter para comenzar
print("\nPractica 19")  # Indica el inicio de la Practica 19
colores = ('rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja')  # Define la tupla de colores
numeros = (10, 1, 5, 11)  # Define la tupla de números
# Muestra información sobre las operaciones a realizar
print("Usando las Tuplas así como con las 2 listas se deben de realizar 2 diferentes acciones")  # Explicación de las acciones a realizar
# Accede al color en la posición 1 (índice 1) de la tupla 'colores'
print("Primero acceder al color en la posición 1 el cual es: ", colores[1])  # Muestra el color en la posición 1
# Realiza una operación matemática usando elementos de la tupla 'numeros'
operacion = numeros[0] + numeros[2] + numeros[3] - numeros[1]  # Suma y resta de elementos de la tupla
# Muestra el resultado de la operación
print("Segundo, se debe realizar una operación con la lista de números dando como resultado el 25: ", operacion)  # Muestra el resultado de la operación
print(input("------Presione Enter Para Pasar A La Siguiente Practica"))  # Solicita al usuario que presione Enter para continuar
os.system("cls")  # Limpia la consola para una mejor visualización

# Practica 20: Como Convertir Tuplas a Listas y Viceversa
print("\nPractica 20")  # Indica el inicio de la Practica 20
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']  # Define la lista de colores
# Muestra la lista de colores actual
print("Usando la siguiente lista debo de convertirla a tupla usando el comando 'tuple':\n", colores)  # Explicación de la conversión
# Convierte la lista 'colores' en una tupla
tupla = tuple(colores)  # Realiza la conversión a tupla
# Muestra la tupla creada a partir de la lista
print("Ahora se mostrara como una tupla: ", tupla)  # Muestra la tupla resultante
# Explica cómo convertir una tupla de vuelta a lista usando el comando 'list'
print("Así mismo si quiero regresar una tupla a una lista usaría el comando 'list(x)'")  # Explicación de la conversión inversa
print(input("------Presione Enter Para Pasar A La Siguiente Practica"))  # Solicita al usuario que presione Enter para continuar
os.system("cls")  # Limpia la consola para una mejor visualización

# Practica 21: El Condicional IF y Operadores de Comparación
print("\nPractica 21")  # Indica el inicio de la Practica 21
print("Se deben de cambiar los operadores para que se conviertan tanto en true como false")  # Explicación de la tarea que se realizará
num1 = 15  # Asigna el valor 15 a num1
num2 = 20  # Asigna el valor 20 a num2

# Comparación usando el operador '!=' (diferente)
if num1 != num2:  # Verifica si num1 es diferente de num2
    print('Se ejecuta el if.', "Se ejecutó porque 15 es diferente de 20")  # Mensaje si la condición es verdadera

num3 = 1450  # Asigna el valor 1450 a num3
num4 = 60    # Asigna el valor 60 a num4

# Comparación usando el operador '>' (mayor que)
if num3 > num4:  # Verifica si num3 es mayor que num4
    print('Se ejecuta el if.', "Se ejecutó porque 1450 es mayor que 60")  # Mensaje si la condición es verdadera

num5 = 1450  # Asigna el valor 1450 a num5
num6 = 60    # Asigna el valor 60 a num6

# Comparación usando el operador '!=' (diferente)
if num5 != num6:  # Verifica si num5 es diferente de num6
    print('Se ejecuta el if.')  # Mensaje si la condición es verdadera

print(input("------Presione Enter Para Pasar A La Siguiente Practica"))  # Solicita al usuario que presione Enter para continuar
os.system("cls")  # Limpia la consola para una mejor visualización

# Practica 22: El Condicional IF Else
print("\nPractica 22")  # Indica el inicio de la Practica 22
print("Para esta práctica se me da un condicional IF Else que se debe corregir, este termina quedando de la siguiente forma: ")  # Explicación de la práctica

color = 'rojo'  # Asigna el valor 'rojo' a la variable color
# Condicional if-else que verifica si el color es 'rojo'
if color == 'rojo':  # Verifica si la variable color es igual a 'rojo'
    print("El color es rojo.")  # Mensaje si la condición es verdadera
else:
    print("El color no es rojo.")  # Mensaje si la condición es falsa

print(input("------Presione Enter Para Pasar A La Siguiente Practica"))  # Solicita al usuario que presione Enter para continuar
os.system("cls")  # Limpia la consola para una mejor visualización

# Practica 23: El condicional if elif else y entrada de datos
print("\nPractica 23")  # Indica el inicio de la Practica 23
print("Al siguiente código añadele un par de rangos de edad. Uno de 18 años hasta 45 y otro de más de 100 años hasta 120")  # Explicación de la práctica

# Solicita la edad del usuario
edad = int(input('¿Cuál es tu edad?\n'))  # Convierte la entrada a un entero
# Verifica si la edad es menor o igual a 0
if edad <= 0:  # Comprueba si la edad es un valor no válido
    print('Nadie puede tener esa edad.')  # Mensaje si la condición es verdadera
# Verifica si la edad está entre 1 y 18 años
elif edad >= 1 and edad <= 18:  # Comprueba si la edad es menor de 18 años
    print('Eres menor de edad.')  # Mensaje si la condición es verdadera
# Verifica si la edad está entre 18 y 45 años
elif edad > 18 and edad <= 45:  # Comprueba si la edad está entre 18 y 45
    print('Eres de joven aun. Sigue así.')  # Mensaje si la condición es verdadera
# Verifica si la edad está entre 45 y 100 años
elif edad > 45 and edad <= 100:  # Comprueba si la edad está entre 45 y 100
    print('Eres Entre Adulto o Mayor de edad.')  # Mensaje si la condición es verdadera
# Verifica si la edad está entre 100 y 120 años
elif edad > 100 and edad <= 120:  # Comprueba si la edad está entre 100 y 120
    print('Felicidades eres de los seres más viejos del planeta. ¿Cómo fue conocer a Moisés?')  # Mensaje si la condición es verdadera
else:  # Si ninguna de las condiciones anteriores se cumple
    print('Edad no válida.')  # Mensaje si la edad no es válida

print(input("------Presione Enter Para Pasar A La Siguiente Practica"))  # Solicita al usuario que presione Enter para continuar
os.system("cls")  # Limpia la consola para una mejor visualización

# Practica 24: Comprobar Datos en Listas y Tuplas
print("\nPractica 24")  # Indica el inicio de la Practica 24
# Solicita al usuario introducir un color y lo convierte a minúsculas
colores = input('Introduce un color:\n').lower()  # Toma el color de entrada del usuario
lista_colores = ['rojo', 'azul', 'verde', 'amarillo']  # Define la lista de colores existentes

# Verifica si el color introducido está en la lista
if colores in lista_colores:  # Comprueba si el color está en la lista
    print(f'El color {colores} sí forma parte de la lista.')  # Mensaje si el color está en la lista
else:
    print("El color introducido no forma parte de la lista")  # Mensaje si el color no está en la lista
    # Pregunta si desea agregar el color a la lista
    agregar = input("\n¿Gustas agregar este color o algún otro color? (s/n)").lower()  # Solicita respuesta para agregar el color
    # Si el usuario desea agregarlo, se añade el color a la lista
    if agregar == 's':  # Comprueba si el usuario respondió afirmativamente
        lista_colores.append(colores)  # Añade el color a la lista
        print(f'\nEl color {colores} ha sido añadido a la nueva lista de colores')  # Mensaje confirmando la adición
    else:
        print("Ah, bueno entonces no quieres ningún color nuevo.")  # Mensaje si el usuario no desea agregar

print(input("------Presione Enter Para Pasar A La Siguiente Practica"))  # Solicita al usuario que presione Enter para continuar
os.system("cls")  # Limpia la consola para una mejor visualización

# Practica 27: El Bucle While
print("\nPractica 27")  # Indica el inicio de la Practica 27
# Descripción de las tareas a realizar
print("Aquí se harán 3 cosas\n1.- Se creará un bucle while hasta que llegue al 15 con incrementos de 5\n ")  # Explica la primera tarea
x = 0  # Inicializa x en 0

# Bucle while que incrementa x de 5 en 5 hasta llegar a 15
while x <= 15:  # Continúa hasta que x sea mayor que 15
    print(x)  # Imprime el valor actual de x
    x += 5  # Incrementa x en 5

print("2.- Crea un bucle while que se ejecute hasta que x valga -100 con decrementos de 20.\n ")  # Explica la segunda tarea
x = 0  # Reinicia x a 0

# Bucle while que decrementa x de 20 en 20 hasta llegar a -100
while x >= -100:  # Continúa hasta que x sea menor que -100
    print(x)  # Imprime el valor actual de x
    x -= 20  # Decrementa x en 20

print("3.- Crea un bucle while que se ejecute hasta que x valga 0 con decrementos de 1 y que muestre en cada ejecución esta frase con el valor de ejecución correspondiente: 'El valor del bucle es 10'")  # Explica la tercera tarea
x = 10  # Inicializa x en 10

# Bucle while que decrementa x de 1 en 1 hasta llegar a 0
while x >= 0:  # Continúa hasta que x sea menor que 0
    print('El valor de x es: ', x)  # Imprime el valor actual de x
    x -= 1  # Decrementa x en 1

print(input("------Presione Enter Para Pasar A La Siguiente Practica"))  # Solicita al usuario que presione Enter para continuar
os.system("cls")  # Limpia la consola para una mejor visualización

# Practica 28: El Bucle While con Condicional IF
print("\nPractica 28")  # Indica el inicio de la Practica 28
x = 0  # Valor inicial de x
# Bucle while que se ejecuta mientras x sea menor o igual a 30
while x <= 30:  # Continúa mientras x sea menor o igual a 30
    x += 1  # Incrementa x en 1 en cada iteración
    # Salta las ejecuciones cuando x es 4, 6 o 10
    if x == 4 or x == 6 or x == 10:  # Comprueba si x es uno de estos valores
        print('Se saltó el valor ', x, ' de x')  # Mensaje indicando que se saltó el valor
        continue  # Salta a la siguiente iteración del bucle
    # Rompe el bucle cuando x es igual a 15
    if x == 15:  # Comprueba si x es 15
        print('Se rompió la ejecución del bucle cuando x valía: ', x)  # Mensaje indicando que el bucle se rompió
        break  # Sale del bucle
    # Imprime el valor de x en cada iteración que no se cumple con los if anteriores
    print(x)  # Muestra el valor actual de x

# Practica 29: El Bucle For
print("\nPractica 29")  # Indica el inicio de la Practica 29
print("Se crea un bucle for que itere la siguiente tupla y muestre una frase como esta en cada iteración: 'El color es: ' + color + '.'")  # Explicación de la tarea
colores = ('rojo', 'azul', 'verde', 'amarillo')  # Define la tupla de colores

# Bucle for que recorre la tupla 'colores'
for x in colores:  # Itera sobre cada color en la tupla
    print('El color es: ' + x + '.')  # Imprime la frase con el color actual

print(input("------Presione Enter Para Pasar A La Siguiente Practica"))  # Solicita al usuario que presione Enter para continuar
os.system("cls")  # Limpia la consola para una mejor visualización

# Practica 30: El Bucle For con range()
print("\nPractica 30")  # Indica el inicio de la Practica 30
print("Crea un bucle for con un range() que vaya desde el valor 7 hasta el valor 700 en saltos de 100. Basta con que imprimas el valor de cada iteración.")  # Explicación de la tarea

# Bucle for que recorre valores desde 7 hasta 700 en incrementos de 100
for x in range(7, 700, 100):  # Utiliza range() para generar los números deseados
    print(x)  # Imprime el valor actual de x

print(input("------Presione Enter Para Pasar A La Siguiente Practica"))  # Solicita al usuario que presione Enter para continuar
os.system("cls")  # Limpia la consola para una mejor visualización
