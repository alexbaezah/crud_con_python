class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"{self.nombre}: ${self.precio}"

class Cajero:
    def __init__(self, productos):
        self.productos = productos
    
    def comprar(self, persona, nombre_producto):
        # Busca el producto en la lista de productos
        producto = None
        for p in self.productos:
            if p.nombre == nombre_producto:
                producto = p
                break
        
        # Si el producto no se encontró, muestra un mensaje de error
        if producto is None:
            print("El producto no se encontró.")
            return
        
        # Si el producto se encontró, verifica si la persona tiene suficiente dinero
        if persona.dinero >= producto.precio:
            # Si la persona tiene suficiente dinero, le descuenta el precio del producto
            # y agrega el producto a la lista de compras de la persona
            persona.dinero -= producto.precio
            persona.compras.append(producto)
            print(f"{persona.nombre} ha comprado {producto}.")
        else:
            # Si la persona no tiene suficiente dinero, muestra un mensaje de error
            print(f"{persona.nombre} no tiene suficiente dinero para comprar {producto}.")

class Persona:
    def __init__(self, nombre, dinero):
        self.nombre = nombre
        self.dinero = dinero
        self.compras = []
    
    def __str__(self):
        return f"{self.nombre} ({self.dinero})"

# Crea una lista de productos
productos = [
    Producto("Pan", 2.5),
    Producto("Leche", 3.5),
    Producto("Jugo", 4.0)
]

# Crea una instancia de la clase Cajero
cajero = Cajero(productos)

# Crea una instancia de la clase Persona
persona = Persona("Juan", 10)

# Imprime la información de la persona
print(persona)

# Realiza una compra
cajero.comprar(persona, "Pan")

# Imprime la información de la persona
print(persona)

# Realiza otra compra
cajero.comprar(persona, "Leche")
