#Create a class Animal with attributes name and sound, and a method make_sound().
class Animal:
    def __init__(self,name ,sound):
        self.name=name
        self.sound=sound
    def make_sound(self):
        return self.sound
#Create a subclass Dog that inherits from Animal and overrides make_sound() to print "Bark!".
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name,"Bark")
    def make_sound(self):
        print(super().make_sound())
        return "bark"
    
#Create an object of Dog and call make_sound().
dog1=Dog("Boobby")
print(dog1.make_sound())

   