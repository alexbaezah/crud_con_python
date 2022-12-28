import perro
import owner
import comida

class Formato:
    def __init__(self, name, perros):
        self.name = name
        self.perros = perros
    
    def list_perros(self):
        for perro in self.perros:
            print(f"el perrito {perro.name} su dueño es {perro.owner.name} ")


owner1 = owner.Person("alex")
dog1 = perro.Dog("lynda", 6, owner1)

mensaje = Formato("siberiano ", [dog1])

mensaje.list_perros()

croquetas = comida.Comida("croquetas", "(perro)")

dog1.comer(croquetas)