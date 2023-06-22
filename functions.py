import math


def motto():
    print("Hello there is our motto")

motto()
motto()
motto()
def vision():
    print("Hello,this is our vision")
vision()

def add():
    x = 10
    y = 20
    z = x + y
    print(z)

add()
add()
add()

def avg(x, y, z):
    average = (x + y + z) / 3
    print("Your average is"+str(average))

avg(12, 56, 24)
avg(84, 12, 30)
avg(21214, 21545, 1654)

def bmiCalc(weight, height):
    bmi = weight / pow(height, 2)
    if bmi <= 18:
        print("underweight")
    elif bmi <= 29:
        print("Normal weight")
    elif bmi <= 34:
        print("Overweight")
    else:
        print("Obese")

bmiCalc(65,2.1)
def grading(totalmarks, totalsubjects):
    grading = (totalmarks / totalsubjects)
    if grading <= 40:
        print("E")
    elif grading <= 50:
        print("D")
    elif grading <= 60:
        print("C")
    elif grading <= 70:
        print("B")
    else:
        print("A")

grading(600, 8)
grading(550, 8)
grading(429, 8)
grading(523, 8)

def login(email, password):
    if email == "user@example.com" and password == "user123":
        grading(523, 8)
    else:
        print("login failed")

login("user@example.com", "user123")

def areOfACircle(radius):
    area = math.pi * pow(radius, 2)
    return area

print(areOfACircle(12))

