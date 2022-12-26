class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"
    
    def presentate(self):
        print(f"mi nombre es {self.name}, {self.bark()} ")

    def edad(self):
        print(f"tengo {self.age} años {self.bark()}")
            

dog1 = Dog("Fido", 3)
dog2 = Dog("Buddy", 5)

print(dog1.name)  # Fido
print(dog2.age)  # 5
dog1.bark()  # Woof!
dog1.presentate() # mi nombre es Fido, Woof!
dog1.edad() # tengo 3 años Woof!