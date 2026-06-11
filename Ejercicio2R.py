 # Ejercicio 2: Tabla de  multiplicar. Muestra la tabla de multiplicar de un número ingresado por el usuario (del 1 al 10)

Num = float(input("Ingresa un número: "))

for N in range (1, 11):
    print(f"{Num} x {N} = {Num*N}")