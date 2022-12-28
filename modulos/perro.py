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