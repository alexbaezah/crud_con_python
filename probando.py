#Por ejemplo, aquí se muestra cómo crear un array de números enteros:

# Creamos una lista de números enteros
numbers = [1, 2, 3, 4, 5]

#También es posible crear arrays de otros tipos de datos, como cadenas de texto:
# Creamos una lista de cadenas de texto
words = ['apple', 'banana', 'cherry']

# Para acceder a los elementos de un array, se puede utilizar su índice. Los índices en Python comienzan en 0, por lo que el primer elemento de un array tiene índice 0, el segundo elemento tiene índice 1, y así sucesivamente.

# Por ejemplo, para acceder al primer elemento del array numbers creado anteriormente, se puede utilizar la siguiente sintaxis:


first_number = numbers[0]

#También es posible utilizar un ciclo for para recorrer todos los elementos de un array y realizar alguna acción con cada uno de ellos. En este caso, se puede utilizar la variable item para hacer referencia al elemento actual del array en cada iteración del ciclo.

#Por ejemplo, aquí se muestra cómo recorrer el array words y mostrar cada elemento por pantalla:

#Copy code
for item in words:
  print(item)

data = [{'name': "alex", 'age': 32}]


#con string format
for item in data:
    print(f"Name: {item['name']}, Age: {item['age']}")

#sin string format
for item in data:
    print(item['name'],item['age'])
    

