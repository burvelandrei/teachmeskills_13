from abc import ABC, abstractmethod


class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = None
        self.pepperoni = None
        self.mushrooms = None
        self.onions = None
        self.bacon = None

    def __str__(self):
        return f"Size: {self.size} см; Cheese: {self.cheese} гр; Pepperoni: {self.pepperoni} гр; Mushrooms: {self.mushrooms} гр; Onions: {self.onions} гр; Bacon: {self.bacon} гр"


class PizzaBuilder(ABC):

    @abstractmethod
    def set_size(self):
        pass

    @abstractmethod
    def add_cheese(self):
        pass

    @abstractmethod
    def add_pepperoni(self):
        pass

    @abstractmethod
    def add_mushrooms(self):
        pass

    @abstractmethod
    def add_onions(self):
        pass

    @abstractmethod
    def add_bacon(self):
        pass

    @abstractmethod
    def get_result(self):
        pass


class CheesePizza(PizzaBuilder):

    def __init__(self):
        self.pizza = Pizza()

    def set_size(self):
        self.pizza.size = 30

    def add_cheese(self):
        self.pizza.cheese = 100

    def add_pepperoni(self):
        self.pizza.pepperoni = 0

    def add_mushrooms(self):
        self.pizza.mushrooms = 0

    def add_onions(self):
        self.pizza.onions = 5

    def add_bacon(self):
        self.pizza.bacon = 0

    def get_result(self):
        return self.pizza


class CheesePizzaBuilder(PizzaBuilder):

    def __init__(self):
        self.pizza = Pizza()

    def set_size(self):
        self.pizza.size = 30

    def add_cheese(self):
        self.pizza.cheese = 100

    def add_pepperoni(self):
        self.pizza.pepperoni = 0

    def add_mushrooms(self):
        self.pizza.mushrooms = 0

    def add_onions(self):
        self.pizza.onions = 5

    def add_bacon(self):
        self.pizza.bacon = 0

    def get_result(self):
        return self.pizza


class MeatPizzaBuilder(PizzaBuilder):

    def __init__(self):
        self.pizza = Pizza()

    def set_size(self):
        self.pizza.size = 30

    def add_cheese(self):
        self.pizza.cheese = 30

    def add_pepperoni(self):
        self.pizza.pepperoni = 50

    def add_mushrooms(self):
        self.pizza.mushrooms = 0

    def add_onions(self):
        self.pizza.onions = 10

    def add_bacon(self):
        self.pizza.bacon = 50

    def get_result(self):
        return self.pizza


class PizzaDirector:

    def __init__(self, builder):
        self._builder = builder

    def cooking_pizza(self):
        self._builder.set_size()
        self._builder.add_cheese()
        self._builder.add_pepperoni()
        self._builder.add_mushrooms()
        self._builder.add_onions()
        self._builder.add_bacon()

    def get_pizza(self):
        return self._builder.get_result()


# Создаём сырную пиццу
cheese_pizza_builder = CheesePizzaBuilder()
director = PizzaDirector(cheese_pizza_builder)
director.cooking_pizza()
cheese_pizza = director.get_pizza()
print(cheese_pizza)

# Создаём мясную пиццу
meat_pizza_builder = MeatPizzaBuilder()
director = PizzaDirector(meat_pizza_builder)
director.cooking_pizza()
meat_pizza = director.get_pizza()
print(meat_pizza)
