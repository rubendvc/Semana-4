
# Ejercicio 5: Números primos / determina si un nemro es primo usando  for con  codicion anidadas




num = int(input("Ingresa un número: "))

if num < 2:
    print("No es primo") # Si es menor que 2 
else:
    es_primo = True  # asume  que es primo 
    for i in range(2, num):  #divisores
        if num % i == 0:
            es_primo = False
            break

    print("Es primo" if es_primo else "No es primo")

