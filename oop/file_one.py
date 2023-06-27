class Fruit:
    def __init__(self, name, colour, size, price):
        self.name = name
        self.colour = colour
        self.size = size
        self.price = price


class Car:
    def __init__(self, model, colour, reg_no, price):
        self.model = model
        self.colour = colour
        self.reg_no = reg_no
        self.price = price

    def brake(self):
        print("Yeah, i can brake")

    def accelerate(self):
        print("Yeah, i can accelerate")


class Employee:
    def __init__(self, name, dept, salary):
        self.name = name
        self.dept =dept
        self.salary =salary

    def login(self):
        print("Hello, i can login")

    def register(self):
        print("Hello, i can register")