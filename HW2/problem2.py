import copy

class Shape:
    def __init__(self):
        pass
    
class Circle(Shape):
    def __init__(self):
        pass
    
class Square(Shape):
    def __init__(self):
        pass
    
class Rectangle(Shape):
    def __init__(self):
        pass
    
class ShapeCache:
    #shapesCache = {}
    
    shapes = { 0: Circle,
               1: Square,
               2: Rectangle }
    
    def __init__(self):
        self.shapesCache = {}
    
    def load(self):
        for i in range(3):
            self.shapesCache[i] = self.shapes[i]()
            
    def getShape(self, id):
        if id in self.shapesCache:
            return copy.deepcopy(self.shapesCache[id])
        else:
            print("Invalid id...")
            
cache = ShapeCache()
cache.load()
square = cache.getShape(1)