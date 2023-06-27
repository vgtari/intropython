from file_one import *
tundaOne = Fruit("Mango", "Yellow", "400g", "Ksh 40")
tundaTwo = Fruit("Apple", "Pink", "250", "Ksh 35")

gariOne = Car("Mazda", "Black", "KDN222J", "kSH 25M")
gariTwo = Car("V8", "Grey", "KDG666V", "kSH 30M")

print(gariOne.reg_no)

gariTwo.accelerate()
gariOne.brake()


empOne = Employee("King", "Secretary", "Ksh 60000")
empTwo = Employee("Avilie", "Manager", "Ksh 80000")

print(empOne.dept)
print(empTwo.salary)

empTwo.login()
empOne.register()

mkubwaOne = Hod("King", "King254@gmail.com", "King123")
mkubwaOne.register()