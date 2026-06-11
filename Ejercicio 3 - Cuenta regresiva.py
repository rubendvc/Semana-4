#Ingreso de numero
num = int(input("Ingrese el numero para iniciar conteo regresivo: "))

#Estructura while
while num > 0:
    print (num)
    num = num - 1
    if num ==0:
        print(f"{num} Conteo regresivo terminado")
    
    