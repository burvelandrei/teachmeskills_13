from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


class AnimalFactory:
    def create_animal(self, name_animal: str):
        if name_animal.lower() == "dog":
            return Dog()
        elif name_animal.lower() == "cat":
            return Cat()
        else:
            raise Exception("Нет такого животного")


factory = AnimalFactory()
dog = factory.create_animal("dog")
print(dog.speak())
meow = factory.create_animal("cat")
print(meow.speak())
