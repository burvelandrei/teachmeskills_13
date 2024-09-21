from abc import ABC, abstractmethod


class Calculator:
    def __init__(self):
        self._strategy = None

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, new_strategy):
        self._strategy = new_strategy

    def calculate(self, number_1, number_2):
        return self._strategy.execute(number_1, number_2)


class Strategy(ABC):
    @abstractmethod
    def execute(self, number_1, number_2):
        pass


class Addition(Strategy):
    def execute(self, number_1, number_2):
        return number_1 + number_2


class Subtraction(Strategy):
    def execute(self, number_1, number_2):
        return number_1 - number_2


class Multiplication(Strategy):
    def execute(self, number_1, number_2):
        return number_1 * number_2


class Division(Strategy):
    def execute(self, number_1, number_2):
        return number_1 / number_2


calc = Calculator()
calc.strategy = Addition()
print(calc.calculate(1, 2))
calc.strategy = Multiplication()
print(calc.calculate(5, 8))
