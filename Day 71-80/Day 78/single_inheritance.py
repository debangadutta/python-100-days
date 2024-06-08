class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Animal sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark!")

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Cat")
        self.breed = breed
    
    def make_sound(self):
        print("Meow!")

    def scratch(self):
        print(f"{self.name} does scratch! Careful!")

dog1 = Dog("Coco", "Golden")
dog1.make_sound()

animal1 = Animal("Ramesh", "Cow")
animal1.make_sound()

# Quick Quiz: Implement a Cat class by using the animal class. Add some methods specific to cat
cat1 = Cat("Sushi", "Persian")
cat1.make_sound()
cat1.scratch()