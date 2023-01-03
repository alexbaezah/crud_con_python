class Tamagotchi:
    def __init__(self, nombre):
        self.__nombre = nombre  # encapsulado, solo se puede acceder a este atributo desde dentro de la clase
        self.energia = 100  
        self.hambre = 0  

    def jugar(self):
        self.energia -= 10
        self.hambre += 5

    def dormir(self):
        self.energia += 10
        self.hambre -= 5

    def comer(self):
        self.hambre -= 10
    
    def obtener_nombre(self):  # método para acceder al atributo encapsulado
        return self.__nombre

class TamagotchiVirtual(Tamagotchi):  # esta clase hereda de Tamagotchi
    def __init__(self, nombre):
        super().__init__(nombre)  # llamamos al constructor de la clase padre


    

class Juego:
    def __init__(self):
        self.tama = TamagotchiVirtual('Pikachu')
        self.juego_terminado = False

    def personaje(self):
                   print("\
         /\\_/\\\n\
        ( o.o )\n\
          >^<\n\
        ")



    def iniciar(self):
        print('Bienvenido al juego de Tamagotchi!')
        print(self.tama.obtener_nombre())
        self.personaje()
        while not self.juego_terminado:
           
            print('1. Jugar')
            print('2. Dormir')
            print('3. Comer')
            print('4. Salir')
            opcion = input('Elige una opción: ')
            if opcion == '1':
                self.tama.jugar()
            elif opcion == '2':
                self.tama.dormir()
            elif opcion == '3':
                self.tama.comer()
            elif opcion == '4':
                self.juego_terminado = True
            else:
                print('Opción inválida')
            print(f'Energía: {self.tama.energia}') 
            print(f'Hambre: {self.tama.hambre}')
            if self.tama.energia == 10 or self.tama.hambre == 30:
                print(f"la energía de {self.tama.obtener_nombre()} está en {self.tama.energia} y su hambre es de {self.tama.hambre}")
                print("es recomendable que coman")
            elif self.tama.energia == 0 or self.tama.hambre == 40:
                print(f"la energía de {self.tama.obtener_nombre()} está en {self.tama.energia} y su hambre es de {self.tama.hambre}")
                print("tu mascota virtual ha perecido")
                self.juego_terminado = True
        print('Gracias por jugar!')


tama = TamagotchiVirtual('Pikachu')
tama.jugar()
tama.dormir()
tama.comer()

juego = Juego()
juego.iniciar()



