# Polymorphism
# Polymorphism allows methods to be defined in a base class and overridden in derived classes, enabling the same method to behave differently based on the object invoking it.

class Bird:
    def fly(self):
        return "Flies"

class Penguin(Bird):
    def fly(self):
        return "Can't fly"

class Sparrow(Bird):
    def fly(self):
        return "Flies high"

def make_it_fly(bird):
    print(bird.fly())

make_it_fly(Sparrow())  # Output: Flies high
make_it_fly(Penguin())  # Output: Can't fly