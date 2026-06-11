#Estructura while que solicita un valor si el valor es "Salir" el programa finaiza
while True:
    val = input("Ingrese 'Salir' para cerrar el programa:  ")
    if val.upper()=='SALIR':
        break

