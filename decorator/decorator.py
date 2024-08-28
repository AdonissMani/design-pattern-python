from typing import *
from abc import ABC, abstractmethod

'''
1. Aggregation: Aggregation: object A contains objects B; B can live without A.
2. Composition: object A consists of objects B; A manages life cycle of B; B can't live without A.

By using the decorator pattern properly, you can dynamically add toppings (or any additional features)
to the pizza objects without modifying the original class or creating an explosion of subclasses.
Each topping simply wraps the pizza it decorates, adding its own cost to the total.
This approach follows the Open/Closed Principle, one of the SOLID principles of object-oriented design,
allowing the behavior of objects to be extended without modifying their code.
'''
class BasePizza(ABC):

    @abstractmethod
    def get_cost(self) -> None:
        pass
    
class Cheese(BasePizza):
    def __init__(self) -> None:
        self.cost = 50 

    def get_cost(self) -> None:
        return self.cost

class VegDelight(BasePizza):
    def __init__(self) -> None:
        self.cost = 100

    def get_cost(self) -> None:
        return self.cost

class Toppings(BasePizza):
    def __init__(self, base: BasePizza) -> None:
        self.base = base

class Pepperoni(Toppings):
    def get_cost(self) -> None:
        self.cost = self.base.get_cost() + 11
        return self.cost
    

class Bacon(Toppings):
    def get_cost(self) -> None:
        self.cost = self.base.get_cost() + 20
        return self.cost


if __name__ == "__main__":

    basePizza = VegDelight()
    pepperoni = Pepperoni(basePizza)
    bacon = Bacon(pepperoni)
    print(bacon.get_cost())

    ## or
    pizza = Bacon(Pepperoni(VegDelight()))
    print(pizza.get_cost())