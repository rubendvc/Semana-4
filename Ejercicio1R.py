# Ejercicio 1: Clasificar Número. Pide un numero al usuraio e indica si es positivo, negativo o cero.

N = int(input("Ingresa un número: "))

if N > 0:
    print(f"El número {N} es positivo.")

elif N < 0:
    print(f"El número {N} es negativo.")

else:
    print("El número es cero.")