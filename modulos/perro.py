from comida import Comida
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
    