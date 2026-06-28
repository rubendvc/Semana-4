# IA_CARRITO

class Cliente:
   
    def __init__(self, nombre, apellidos, dni, telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.telefono = telefono

  
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre} {self.apellidos}")
        print(f"DNI: {self.dni} - Teléfono: {self.telefono}")


class Producto:
    def __init__(self, id_producto, nombre, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio


class Carrito:
    def __init__(self, cliente):
        self.cliente = cliente
        self.lista_compras = [] 

    def agregar_producto(self, producto, cantidad):
        subtotal = producto.precio * cantidad
        
        item = {
            "producto": producto,
            "cantidad": cantidad,
            "subtotal": subtotal
        }
        self.lista_compras.append(item)

    def mostrar_resumen(self):
        print("\n========================================")
        print("          RESUMEN DE SU COMPRA          ")
        print("========================================")
        
        
        print("--- DATOS DEL CLIENTE ---")
        self.cliente.mostrar_datos()
        
        print("\n--- PRODUCTOS COMPRADOS ---")
        total_compra = 0
        
        
        for item in self.lista_compras:
            prod = item["producto"]
            cant = item["cantidad"]
            sub = item["subtotal"]
            
            
            total_compra = total_compra + sub 
            
            print(f"- {prod.nombre} | Precio: S/{prod.precio} | Cantidad: {cant} | Subtotal: S/{sub}")
            
        print("\n========================================")
        print(f"TOTAL A PAGAR: S/{total_compra}")
        print("========================================")


# ==========================================
# 2. PROGRAMA PRINCIPAL (Lógica e Interacción)
# ==========================================

print("=== BIENVENIDO AL SISTEMA DE VENTAS ===")


nom = input("Ingrese su nombre: ")
ape = input("Ingrese su apellidos: ")
doc = input("Ingrese su numero de DNI: ")
tel = input("Ingrese su teléfono: ")


cliente_actual = Cliente(nom, ape, doc, tel)
mi_carrito = Carrito(cliente_actual)


catalogo = [
    Producto("1", "Polo de Algodón", 25.0),
    Producto("2", "Pantalón Jean  ", 65.0),
    Producto("3", "Zapatillas     ", 120.0),
    Producto("4", "Gorra          ", 15.0)
]


while True:
    print("\n--- LISTA DE PRODUCTOS ---")
    print("ID   | NOMBRE           | PRECIO")
    print("---------------------------------")
    
    
    for p in catalogo:
        print(f"{p.id_producto}    | {p.nombre}  | S/{p.precio}")
        
    print("---------------------------------")
    
    
    seleccion = input("Ingrese el ID del producto que desea comprar (o escriba 'salir'): ")
    
    
    if seleccion.lower() == "salir":
        break
        
    
    producto_encontrado = None
    for p in catalogo:
        if p.id_producto == seleccion:
            producto_encontrado = p
            break 
            
    
    if producto_encontrado != None:
        cantidad_texto = input(f"¿Cuántas unidades de '{producto_encontrado.nombre}' desea?: ")
        cantidad = int(cantidad_texto) 
        
        
        mi_carrito.agregar_producto(producto_encontrado, cantidad)
        print("--> ¡Producto agregado correctamente al carrito!")
    else:
        print("--> Error: El ID ingresado no existe. Intente de nuevo.")


mi_carrito.mostrar_resumen()