# Ejercicio 4: Menú de opciones. Crea un menú que se repita hasta que el usuario elija 'Salir' (do-while).

while True:
    sal = input("Escribe 'salir' para terminar: ")

    if sal.lower() == 'salir':
        print("Saliste")
        break