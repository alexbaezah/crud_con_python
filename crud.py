# Creamos una lista para almacenar los datos
data = []

def create(name, age):
  # Añadimos un nuevo elemento a la lista con la información del usuario
  data.append({'name': name, 'age': age})

def read():
  # Recorremos la lista y mostramos la información de cada usuario
  for item in data:
    print(f"Name: {item['name']}, Age: {item['age']}")

def update(name, age):
  # Recorremos la lista y buscamos el usuario con el nombre especificado
  for item in data:
    if item['name'] == name:
      # Actualizamos la edad del usuario
      item['age'] = age
      break

def delete(name):
  # Recorremos la lista y buscamos el usuario con el nombre especificado
  for item in data:
    if item['name'] == name:
      # Eliminamos el usuario de la lista
      data.remove(item)
      break

# Creamos algunos usuarios
create("John", 30)
create("Jane", 25)
create("Mike", 35)

# Mostramos la información de todos los usuarios
read()

# Actualizamos la edad de Jane
update("Jane", 28)

# Eliminamos a Mike
delete("Mike")

# Mostramos de nuevo la información de todos los usuarios
read()

def findByName(name):
  # Recorremos la lista y buscamos el usuario con el nombre especificado
  for item in data:
    if item['name'] == name:
      print(f"nombre: {item['name']}, edad: {item['age']}")
      break
    else:
        print(f"No se ha encontrado el nombre:{ name}")
        break

findByName("John")
findByName("Alexa")