class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"\nName: {self.name}")
        print(f"Species: {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def show_details(self):
        super().show_details()
        print(f"Breed: {self.breed}")

class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
    
    def show_details(self):
        super().show_details()
        print(f"Color: {self.color}")

goldy1 = GoldenRetriever("Coco", "Golden Brown")
goldy1.show_details()

doggy1 = Dog("Coconut", "Goldy Boy")
doggy1.show_details()

animal1 = Animal("Nemo", "Catto")
animal1.show_details()

print(f"\nMRO of GoldenRetriever: {GoldenRetriever.mro()}")