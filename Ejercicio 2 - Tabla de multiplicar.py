#Ingreso de dato
num = int(input("Ingrese un numero para multiplicar : "))
#Creación del rango por el cual se va a multiplicar el numero
for i in range(1,11):
    print(f"{num} * {i:2} = {num*i:3}")
#El numero :2 y :3 reserva un espacio de 2 y 3 caracteres sin importar si el numero es grande o pequeño

