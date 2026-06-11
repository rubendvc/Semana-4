# ejercicio7.py
#  Validar contraseña con  while; maximo 3 intentos,bloquea si falla
# ===============================================================
Password_correcta = "2000"
intentos = 0

while intentos < 3:
    Password = input("Ingrese la contraseña: ")  # Condicion maximo 3 intentos

    if Password == Password_correcta:
        print(" Acceso concedido")
        break 
    else:
        intentos += 1
        print(f"Contraseña incorrecta. Intento {intentos}/3")

        if intentos < 3:
            print("Intente nuevamente")

# Verifica  intentos de bloqueo
if intentos == 3:
    print(" Acceso bloqueado")