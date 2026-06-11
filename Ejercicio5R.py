# Ejercicio 5: Números primos. Determina si un numero es primo usando for con condicionales anidadas.

Num = int(input("Ingresa un  número: "))

if Num < 2:
    print(f"El numero {Num} no es primo, debe ser mayor a 1")

else:
    for n in range (2, Num):
        if Num % n == 0:
            print(f"El número {Num} no es primo")
            break
    else:
        print(f"El número {Num} es primo")
            