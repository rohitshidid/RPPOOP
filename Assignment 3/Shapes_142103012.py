from abc import ABC, abstractmethod
import math
from tkinter import *
from tkinter.ttk import *

class shapes(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class ellipse(shapes):
    def __init__(self, radius1, radius2):
        self.radius1 = radius1
        self.radius2 = radius2
        pass

    def draw(self):
        master = Tk()
        master.title("Shapes")
        canvas = Canvas(master)
        canvas.create_oval(130, 30, 230, 100, outline = "red", width = 2)
        canvas.pack(fill = BOTH, expand = 1)
        mainloop()
        pass

    def area(self, ):
        print("Area Of Ellipse is {0}".format(math.pi * self.radius1 * self.radius2))
        pass

    def perimeter(self):
        perimeter_ellipse = math.pi * (3 * (self.radius1 + self.radius2) - math.sqrt((3 * self.radius1 + self.radius2) * (self.radius1 + 3 * self.radius2)))
        print("Approximiate Perimeter Of Ellipse is {0}".format(perimeter_ellipse))
        pass

class circle(shapes):
    def __init__(self, radius):
        self.radius = radius
        pass

    def draw(self):
        master = Tk()
        master.title("Shapes")
        canvas = Canvas(master)
        canvas.create_oval(20, 20, 90, 90, outline = "black", width = 4)
        canvas.pack(fill = BOTH, expand = 1)
        mainloop()
        pass

    def area(self):
        print("Area Of Circle is {0}".format(math.pi * self.radius * self.radius))
        pass

    def perimeter(self):
        print("Perimeter Of Circle is {0}".format(2 * math.pi * self.radius))
        pass

class rectangle(shapes):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        pass

    def draw(self):
        master = Tk()
        master.title("Shapes")
        canvas = Canvas(master)
        canvas.create_rectangle(230, 10, 310, 60, outline = "red", width = 4)
        canvas.pack(fill = BOTH, expand = 1)
        mainloop()
        pass

    def area(self):
        print("Area Of Rectangle is {0}".format(self.length * self.width))
        pass

    def perimeter(self):
        print("Perimeter Of Rectangle is {0}".format(2 * (self.length * self.width)))
        pass

class triangle(shapes):
    def __init__(self, base, height):
        self.height = height
        self.base = base
        pass

    def draw(self):
        master = Tk()
        master.title("Shapes")
        canvas = Canvas(master)
        canvas.create_polygon((50, 150, 100, 50, 150, 150))
        canvas.pack(fill = BOTH, expand = 1)
        mainloop()
        pass

    def area(self):
        print("Area Of Triangle is {0}".format((self.base * self.height) / 2))
        pass

    def perimeter(self, side1, side2, side3):
        print("Perimeter Of Triangle is {0}".format(side1 + side2 + side3))
        pass

class square(shapes):
    def __init__(self, side):
        self.side = side
        pass
        
    def draw(self):
        master = Tk()
        master.title("Shapes")
        canvas = Canvas(master)
        canvas.create_rectangle(250, 30, 310, 90, outline = "black", width = 4)
        canvas.pack(fill = BOTH, expand = 1)
        mainloop()
        pass

    def area(self):
        print("Area Of Square is {0}".format(self.side * self.side))
        pass

    def perimeter(self):
        print("Perimeter Of Square is {0}".format(4 * self.side))
        pass


t = triangle(10, 10)
t.area()
t.perimeter(10, 20, 30)
t.draw()

r = rectangle(50, 50)
r.area()
r.perimeter()
r.draw()

c = circle(5)
c.area()
c.perimeter()
c.draw()

s = square(5)
s.area()
s.perimeter()
s.draw()

e = ellipse(60, 60)
e.area()
e.perimeter()
e.draw()
