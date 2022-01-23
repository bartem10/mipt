class Shape():

    def __init__(self, width, height):
        self.width = width
        self.height = height

class Triagle(Shape):

    def area(self):
        return 0.5 * self.width * self.height

class Rectangle(Shape):

    def area(self):
        return self.width * self.height

if __name__ == "__main__":
    t = Triagle(2, 6)
    r = Rectangle(2, 6)
    print(t.area(), r.area())