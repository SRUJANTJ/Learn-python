# Polymorphism
#  Polymorphism means many forms. It allows the same method name to have different
#  implementations.
class Cat:
    def sound(self):
        print("Meow")
class Cow:
    def sound(self):
        print("Moo")
def animal_sound(animal):
    animal.sound()
cat = Cat()
cow = Cow()
animal_sound(cat)
animal_sound(cow)