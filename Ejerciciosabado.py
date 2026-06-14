#SOLICITAR PRIMER NUMERO
while True:
    num1 = int(input("Ingrese el pirmer numero a evaluar:  "))
    if num1 > 0:
        break
#SOLICITAR OPERACIÓN
while True:
    print("Ingrese una opcion entre 1 - 8")
    print("1 - Suma")
    print("2 - Resta")
    print("3 - Multiplicación")
    print("4 - División")
    print("5 - Elevar al cuadrado")
    print("6 - Factorial")
    print("7 - Conjetura de Collatz")
    print("8 - Hallar los 'n' primeros numeros primos")
    opcion = int(input())

    if opcion > 0 and opcion <= 4:
        num2 = int(input("Ingrese el segundo número a operar: "))