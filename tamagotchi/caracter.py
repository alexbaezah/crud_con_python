def generar_lista(caracter, longitud):
  lista = [caracter] * longitud
  cadena = "".join(lista)
  return [cadena]

lista = generar_lista("*", 5)
print(lista) # Imprime: ['*', '*', '*', '*', '*']

def dragon():
    print("\
     /\_/\\\n\
    | o o |\n\
    |   ^ |\n\
    | \_/ |\n\
     \___/\
")

def gato():
    print("\
 /\\_/\\\n\
( o.o )\n\
  >^<\n\
")

dragon()
gato()

opciones = ['opción 1', 'opción 2', 'opción 3', 'salir']

while True:
    print("Selecciona una opción:")
    for i in range(len(opciones)):
        print(f"{i+1}. {opciones[i]}")
    opcion = input()

    if opcion == '1':
       print("opción 1")
    elif opcion == '2':
      print("opción 2")        
    elif opcion == '3':
      print("opción 3")
    elif opcion == '4':
      break

class Tamagotchi: 
    def __init__(self, nombre, energia, hambre, limpieza):
        self.nombre = nombre
        self.energia = energia 
        self.hambre = hambre 
        self.limpieza = limpieza 

    def comer():
        return ""
    
    def dormir():
        return ""
    
    def limpiar():
        return ""
    
    def jugar():
        return ""

class Opcion:
  def __init__(self, tamagotchi):
    self.tamagotchi = tamagotchi
  
  def 
     