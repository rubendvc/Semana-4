def suma():
    return num1 + num2

def resta():
    return num1 - num2

def multiplicacion():
    return num1 * num2

def division():
    return num1 / num2

def cuadrado():
    return num1 ** num1

def factorial():
    return num1
    
def collatz():
    def es_par():
        return num // 2
    
    def es_impar():
        return num*3+1
    
    while num > 1:
        if num % 2 == 0:
            num = es_par()
            print(num)
        else:
            num = es_impar()
            print(num)

def primos():
    if num1 < 2:
     print(f"El numero {num1} no es primo, debe ser mayor a 1")

    else:
        for n in range (2, Num):
            if num1 % n == 0:
                print(f"El número {num1} no es primo")
                break
        else:
            print(f"El número {num1} es primo")

num1 = int(input("Ingrese un numero: "))

while True:
    print("i) Suma")
    print("ii) Resta")
    print("iii) Multiplicación")
    print("iv) Division")
    print("v) Elevar al cuadrado")
    print("vi) Factorial")
    print("vii) Conjetura de Collatz")
    print("viii) Hallar los 'n' primeros numeros")
    opcion = input("ingresa una opcion: ")
    if opcion.lower() == 'i':
        num2 = int(input("Ingresa el segundo numero: "))
        print (suma())
        break
    
    if opcion.lower() == 'ii':
        num2 = int(input("Ingresa el segundo numero: "))
        print(resta())
        break

    if opcion.lower() == 'iii':
        num2 = int(input("Ingresa el segundo numero: "))
        print(multiplicacion())
        break

    if opcion.lower() == 'iv':
        num2 = int(input("Ingresa el segundo numero: "))
        print(division())
        break

    if opcion.lower() == 'v':
        print(cuadrado())
        break

    if opcion.lower() == 'vi':
        print(factorial())
        break

    if opcion.lower() == 'vii':
        print(collatz())
        break

    if opcion.lower() == 'viii':
        print(primos())
        break

# while True:
#     menu = input("Ingresa una opcion: ")

#     if menu() == 'salir':
#         print("Saliste")
#         break
