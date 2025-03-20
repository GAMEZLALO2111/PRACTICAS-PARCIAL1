import os  # Importa el módulo os para poder limpiar la consola

# Practica 10: Cómo Crear Listas y Utilizarlas en Python
print(input("------ Presione Enter Para Iniciar ------"))  # Solicita al usuario que presione Enter para comenzar
print("\nPractica 10")  # Indica el inicio de la Practica 10
# Definimos una lista de colores
colores = ["rojo", "azul", "verde", "amarillo", "marrón", "lila", "negro", "rosa"]  # Lista de colores
print("De esta lista: ", colores, "\nEl que esta en la posicion numero 3 es: ")  # Imprime la lista de colores y un mensaje
# Imprimimos el color en la posición 3 (amarillo)
print(colores[3])  # Muestra el color en la posición 3 (amarillo)
# Informamos las posiciones de rojo y rosa
print("Asi mismo los colores rojo y rosa se encuentran en la posicion 0 y 7 respectivamente")  # Explica las posiciones de los colores rojo y rosa
print(input("------ Presione Enter Para Continuar ------"))  # Solicita al usuario que presione Enter para continuar
os.system("cls")  # Limpia la consola para una mejor visualización

# Practica 11: Posiciones Negativas en Listas Python
print("\nPractica 11")  # Indica el inicio de la Practica 11
# Otra lista de colores
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']  # Lista de colores
print("Mediante las listas negativas, imprimire 5 de los siguientes colores: ", colores)  # Muestra la lista de colores
# Imprimimos colores usando posiciones negativas
print(colores[-1])   # Imprime 'naranja', el último color en la lista
print(colores[-7])   # Imprime 'lila', el cuarto color desde el final
print(colores[-5])   # Imprime 'marrón', el sexto color desde el final
print(colores[-2])   # Imprime 'blanco', el segundo color desde el final
print(colores[-10])  # Imprime 'rojo', el primer color en la lista
print("Se imprimio cada color dependiendo de su posicion negativa, como ejemplo se ve asi 'print(colores[-1])'")  # Explicación de la impresión por posición negativa
print(input("------ Presione Enter Para Continuar ------"))  # Solicita al usuario que presione Enter para continuar
os.system("cls")  # Limpia la consola para una mejor visualización

# Practica 12: Eliminar Elementos con del()
print("\nPractica 12")  # Indica el inicio de la Practica 12
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']  # Lista de colores
print("De la siguiente lista, usando el comando 'del' debo de elimiar elementos: ", colores)  # Muestra la lista original
# Eliminamos elementos usando sus posiciones
del colores[-9]  # Elimina 'rojo', que está en la primera posición
del colores[4]   # Elimina 'marrón', que está en la quinta posición
del colores[-4]  # Elimina 'negro', que está en la cuarta posición desde el final
del colores[-3]  # Elimina 'rosa', que está en la tercera posición desde el final
print("Ahora se impimira la lista sin los elementos que se debian de eliminar", colores)  # Muestra la lista después de eliminar los elementos
print(input("------ Presione Enter Para Continuar ------"))  # Solicita al usuario que presione Enter para continuar
os.system("cls")  # Limpia la consola para una mejor visualización

# Practica 13: Eliminar Elementos con remove()
print("\nPractica 13")  # Indica el inicio de la Practica 13
print("De la siguiente lista de colores se debe de eliminar elementos usando unicamente 'remove': ", colores)  # Muestra la lista original antes de definirla
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']  # Define la lista de colores
# Usamos 'remove' para eliminar elementos por su valor
colores.remove('amarillo')  # Elimina 'amarillo' de la lista
colores.remove('rojo')      # Elimina 'rojo' de la lista
print("Ahora se imprimira la lista sin los colores que se eliminaron usando el 'remove': ", colores)  # Muestra la lista después de eliminaciones
print(input("------ Presione Enter Para Continuar ------"))  # Solicita al usuario que presione Enter para continuar
os.system("cls")  # Limpia la consola para una mejor visualización

# Practica 14: Eliminar Elementos con pop()
print("\nPractica 14")  # Indica el inicio de la Practica 14
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']  # Define la lista de colores
print("Usando el metodo 'pop', debo de eliminar 2 elementos asi mismo se deben de almacenar")  # Mensaje que explica la acción
# Eliminamos y almacenamos colores usando 'pop'
color1 = colores.pop(1)  # Elimina 'azul' de la posición 1 y lo almacena en 'color1'
color2 = colores.pop(7)  # Elimina 'rosa' de la posición 7 y lo almacena en 'color2'
print("Ahora se imprimiran los valores eliminados y guardados: ", color1, color2)  # Muestra los colores eliminados y almacenados
print(input("------ Presione Enter Para Continuar ------"))  # Solicita al usuario que presione Enter para continuar
os.system("cls")  # Limpia la consola para una mejor visualización

# Practica 15: Insertar Elementos con append()
print("\nPractica 15")  # Indica el inicio de la Practica 15
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']  # Define la lista de colores
print("De la siguiente lista, debere añadir 2 colores los cuales son 'fuxia' y 'celeste': ", colores)  # Mensaje que explica la acción
# Añadimos nuevos colores al final de la lista
colores.append('fuxia')   # Agrega 'fuxia' al final de la lista
colores.append('celeste')  # Agrega 'celeste' al final de la lista
print("Ahora aparecera la lista de los colores con los 2 que se agregaron: ", colores)  # Muestra la lista actualizada con los nuevos colores
print(input("------ Presione Enter Para Continuar ------"))  # Solicita al usuario que presione Enter para continuar
os.system("cls")  # Limpia la consola para una mejor visualización

# Practica 16: Insertar Elementos con insert()
print("\nPractica 16")  # Indica el inicio de la Practica 16
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']  # Define la lista de colores
print("De la siguiente lista, debere añadir 2 colores usando el metodo 'insert' en dos posiciones diferentes: ", colores)  # Mensaje que explica la acción
# Insertamos colores en posiciones específicas
colores.insert(6, 'magenta')   # Inserta 'magenta' en la posición 6
colores.insert(-1, 'turquesa')  # Inserta 'turquesa' justo antes de 'naranja'
print("Ahora la lista se vera modificada con los 2 nuevos colores que se agregaron en 2 posiciones especifias: ", colores)  # Muestra la lista actualizada con los nuevos colores
print(input("------ Presione Enter Para Continuar ------"))  # Solicita al usuario que presione Enter para continuar
os.system("cls")  # Limpia la consola para una mejor visualización

# Practica 17: Ordenar Elementos con sort() y sorted()
print("\nPractica 17")  # Indica el inicio de la Practica 17
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']  # Define la lista de colores
print("De la siguiente lista se deben de acomodar los nombres den orden alfabetico de forma descendente: ", colores)  # Mensaje que explica la acción
# Ordenamos la lista en orden descendente
colores.sort(reverse=True)  # Ordena la lista de colores en orden descendente
# Obtenemos la cantidad de colores
cantidad_colores = len(colores)  # Cuenta el número de colores en la lista
print("Ahora se impiran en orden alfabetico de la z - a: ", colores)  # Muestra la lista ordenada
print("Adicionalmente mencionare la cantidad de colores que hay en la lista: ", cantidad_colores)  # Muestra la cantidad de colores en la lista
print(input("------ Presione Enter Para Terminar ------"))  # Solicita al usuario que presione Enter para finalizar
os.system("cls")  # Limpia la consola para una mejor visualización

