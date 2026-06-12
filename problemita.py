# num = int(input("Ingresa un numero entero positivo: "))
# while num < 0:
#         print("numero incorrecto")
#         num = int(input("Ingresa un numero entero positivo: "))


# 
while True:
       num = int(input("Ingrese un numero entero positivo mayor a 1: "))
       if num > 1:
        break
print (num)
# Creamos el bucle hasta que el numero sea = 1
while num != 1:
        # Evaluamos si es par, dividimos entre 2
        if num % 2 == 0:
                num = num / 2
        else: 
            num = num * 3 + 1

        print(f"{num:.0f}")