class Dog:
    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        self.owner = owner

    def bark(self):
        return "Woof!"
    
    def presentate(self):
        print(f"mi nombre es {self.name}, {self.bark()} ")

    def edad(self):
        print(f"tengo {self.age} años {self.bark()}")
    
    def comer(self, comida):
        #sinstance devuelve True si obj es una instancia de la clase cls o 
        # de una de sus subclases, y False en caso contrario.
        if isinstance(comida, Comida):
            self.comida = comida 
            print(f"{self.name} está comiendo {comida}.")
        else:
            print("La comida no es válida.")


class Person:
    def __init__(self, name):
        self.name = name
    
    def presentate(self):
        
        print(f"mi nombre es {self.name} ")

class Formato:
    def __init__(self, name, perros):
        self.name = name
        self.perros = perros
    
    def list_perros(self):
        for perro in self.perros:
            print(f"el perrito {perro.name} su dueño es {perro.owner.name} ")

class Comida:
    def __init__(self, name, type):
        self.name = name 
        self.type = type
    
    def __str__(self):
        return f"{self.name} ({self.type})"
    
    




alex = Person("Alex")
pati = Person("Pati")

john = Person("John")



            

dog1 = Dog("Fido", 3, alex)
dog2 = Dog("Buddy", 5, pati)
nombre = dog1.name

print(dog1.name)  # Fido
print(dog2.age)  # 5
dog1.bark()  # Woof!
dog1.presentate() # mi nombre es Fido, Woof!
dog1.edad() # tengo 3 años Woof!
dog1.owner.presentate() # mi nombre es Alex
dog2.owner.presentate() # mi nombre es Pati

formato = Formato("peludos", [dog1, dog2])

formato.list_perros()

croquetas = Comida("croquetas", "perro")

dog1.comer(croquetas)