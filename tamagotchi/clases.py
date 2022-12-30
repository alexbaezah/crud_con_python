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

class Juego:
    def __init__(self, tamagotchi):
        self.tamagotchi = tamagotchi
    
    def  iniciar(self, tamagotchi):  
        comienzo = isinstance(tamagotchi, Tamagotchi)
        while comienzo:
            print("esto funciona") 
            comienzo =  False 




dragon = Tamagotchi("Lynda", 10, 5, 4)
inicio = Juego(dragon)
inicio.iniciar(dragon)
            

    
