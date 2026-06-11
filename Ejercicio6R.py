# Ejercicio 6: Piramide de asteriscos. Dibuja una pirámide de N filas usando bucles for anidados.

Num = int(input("Ingresa un número: "))

for N in range (Num +1):
    

    for B in range (2 * N - 1):
        print("*", end="")


    print()
  