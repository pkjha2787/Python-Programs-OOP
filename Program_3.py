#Create a class Parent with an __init__ method that initializes name.
class Parent:
    def __init__(self,name):
        self.name=name

#Create a class Child that inherits from Parent, and in its __init__, use super() to initialize name and also add an extra attribute age.

class Child(Parent):
    def __init__(self, name,age):
        super().__init__(name)
        self.age=age
#Create an object of Child and print both name and age.

child1=Child("Pragya",37)
print(child1.name,child1.age)