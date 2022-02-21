class Shape:
  def Draw(self):
    print("Shape")

class Circle(Shape):
  def Draw(self):
    print("Circle")

class Square(Shape):
  def Draw(self):
    print("Square")

class Triangle(Shape):
  def Draw(self):
    print("Triangle")

#Before

circle = Circle()
circle.Draw()
square = Square()
square.Draw()
triangle = Triangle()
triangle.Draw()

#After

class ShapeFactory:
  def __init__(self):
    self.shapes = { "Circle": Circle, 
                    "Square": Square,
                    "Triangle": Triangle }

  def create(self, shape):
    return self.shapes[shape]()

s = ShapeFactory()
circle = s.create("Circle")
circle.Draw()
square = s.create("Square")
square.Draw()
triangle = s.create("Triangle")
triangle.Draw()

#Client function

class Client:
  def draw(self):
    shapes = { "1": "Circle",
               "2": "Square",
               "3": "Triangle" }
    x = input("Choose the shape:\nCircle - 1\nSquare - 2\nTriangle - 3\n")
    if x in shapes: 
      ShapeFactory().create(shapes[x]).Draw()
    else:
      print("Invalid number...")

client = Client()
client.draw()
