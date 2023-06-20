age = 18
if age < 18:
    print("TRUE")
else:
    print("FALSE")
x = 10
y = 20
if x < y and y > 30:
    print("TRUE")
else:
    print("FALSE")
    if x < y or y > 50:
        print("TRUE")
    else:
        print("FALSE")

        marks = 90
        if marks < 40:
            print("E")
        elif marks < 50:
            print("D")
        elif marks < 60:
            print("C")
        elif marks < 70:
            print("B")
        else:
            print("A")

bettingNumber = 0
if bettingNumber == 1:
    print("You won a goat!!")
elif bettingNumber == 2:
    print("You won a cow!!")
elif bettingNumber == 3:
    print("You won 3 cows!!")
elif bettingNumber == 4:
    print("You won 5 cows!!")
else:
    print("Please enter a number from 1-4 to bet!!")


p =50000
r = 10
t = 5
interest = (p * r * t) / 100

if interest <= 20000:
    print("GOOD LOAN")
elif interest <= 40000:
    print("BAD LOAN")
else:
    print("SCAM")

weight = 86
height = 1.8
BMI = (weight / (height * height))
if BMI <= 18:
    print("UNDERWEIGHT")
elif BMI <= 29:
    print("NORMAL WEIGHT")
elif BMI <= 34:
    print("OVER WEIGHT")
else:
    print("OBESE")



