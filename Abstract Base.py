from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 4
        self.beadth = 6

    def printarea(self):
        return self.length * self.beadth

rect1 = Rectangle()
print(rect1.printarea())

#Shape class ka object nahi bana sakte ismien