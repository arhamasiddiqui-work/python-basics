# OOP(object oriented programming)
# we create classes that are blueprint(refers to a class which defines the structure and behavior of objects allowing for code reuse and organization) then create objects, to map real world scenarios


class Student:
    # default constructor
    def __init__(self):
        pass

    # parameterized constructor
    school_name = "ABC School"  # class variable,shared by all objects of the class

    def __init__(
        self, name
    ):  # self parameter is used to access diff variables that belong to the class & used by objects
        self.name = name  # instance variable
        print("Adding a new student...")


s1 = Student("Random")
print(s1.name)
print(Student.school_name)

# Methods: function that belong to obj

# 3 types: staticmethod, classmethod(cls), instancemethod(self)


# Instance method: self parameter is used
class Car:
    Brand = "BMW"  # class variable
    name = input("Enter your name: ")

    def __init__(self, model, price):
        self.model = model  # instance variable
        self.price = price  # instance variable

    def Welcome(self):  # creating a method inside a class
        print("Welcome! to my car showroom Dear:", self.name)


car1 = Car("X5", 100000000)
car1.Welcome()  # calling the method using the object
print(car1.model, car1.price)
print(Car.Brand)


class Person:
    name = "anonymous"

    def changeName(self, name):
        self.name = name  # will create a new name

    #  self.__class__.name=name     # will change in the main class(1 way)
    #   Person.name=name          # will change in the main class(2 way)


p1 = Person()
p1.changeName("Random")
print(p1.name)


# Static Methods: methods that dont use self/cls paramater, can be called using class name,
class Student:
    @staticmethod
    def Hello():
        print("Hello! Students")


Student.Hello()


# CLASS METHODS: method bound to class & receive class as first argument,
class Student:
    name = "Random"

    @classmethod
    def changeName(cls, name):
        cls.name = name


st1 = Student()
st1.changeName("Shraddha")
print(st1.name)


# Property decorator: use methods as attribute
class Student:
    def __init__(self, phy, chem):
        self.phy = phy
        self.chem = chem

    @property
    def percentage(self):
        return str((self.phy + self.chem) / 3) + "%"


st1 = Student(90, 80)
print(st1.percentage)

st1.phy = 75
print(st1.percentage)


# OOP 4 Important Pillars:


# 1- Abstraction: hiding unnecessary details, showing only essential features to the user
# example: create a car class with method to start the car The user only needs to know how to use this methods without knowing the internal details of how they work.
class Car:
    def __init__(self):
        self.brake = False
        self.engine = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.engine = True
        print("Car started...")


car1 = Car()
car1.start()


# 2- Encapsulation: wrapping data and function in single object
# example: the code we write normally in OOP


# 3- Inheritance: when one class(child/derived) derives properties of another class(parent/base)
# SINGLE INHERITANCE:
class Car:
    @staticmethod
    def start():
        print("Car Started..")

    @staticmethod
    def stop():
        print("Car Stopped..")


class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name


car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.start())
print(car1.name)


# # MULTI-LEVEL INHERITANCE:
class Car:
    @staticmethod
    def start():
        print("Car Started..")

    @staticmethod
    def stop():
        print("Car Stopped..")


class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand


class fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type


car1 = fortuner("diesal")
car1.start()


# # MULTIPLE INHERITANCE
class A:
    varA = "Welcome to class A"


class B:
    varB = "Welcome to class B"


class C(A, B):
    varC = "Welcome to class C"


c1 = C()
print(c1.varC, c1.varB, c1.varA)


#  SUPER METHOD: access methods of parent class
class Car:
    def __init__(self, fueltype):
        self.fueltype = fueltype

    @staticmethod
    def start():
        print("Car Started..")

    @staticmethod
    def stop():
        print("Car Stopped..")


class ToyotaCar(Car):
    def __init__(self, name, fueltype):
        self.name = name
        super().__init__(fueltype)
        super().start
        super().stop


car1 = ToyotaCar("fortuner", "electric")
print(car1.fueltype)


# 4- Polymorphism: allows one action to have many forms / same operator diff meaning according to context

print(1 + 2)  # 3
print("testing" + "working")  # concatenate
print([1, 2, 3] + [4, 5, 6])  # merge


# using Operators & dunder function in polymorphism,
# e.g: complex number (1 is real part, 2 is imaginary part)
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    # using Operators & dunder function (__add__)
    def __add__(num1, num2):
        newReal = num1.real + num2.real
        newImg = num1.img + num2.img
        return Complex(newReal, newImg)

    # using Operators & dunder function (__sub__)
    def __sub__(num1, num2):
        newReal = num1.real - num2.real
        newImg = num1.img - num2.img
        return Complex(newReal, newImg)


num1 = Complex(5, 4)
num1.showNumber()

num2 = Complex(2, 4)
num2.showNumber()

numAdd = num1 + num2
numAdd.showNumber()

numSub = num1 - num2
numSub.showNumber()


# Deleting Object:
class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("Random")
del s1
print(s1)

# Public vs Private Modifiers:
# Public: can be accessed from anywhere (normally used),
# Private:can only be accessed within the class(for security/priv purpose)


class Account:
    def __init__(self, acc_no, password):
        self.acc_no = acc_no  # public
        self.__password = password  # private

    def reset_pass(self):
        print(self.__password)  # priv within the class will work


acc1 = Account("USER", "12345")
print(acc1.acc_no)
print(acc1.__password)  # priv outside the class won't work


class Person:
    __name = "Anonymous"


p1 = Person()
print(p1.__name)  # will throw error as __name is priv


# Practice Questions:
# creating student class with methods to calculate average marks of a student
class Student:
    def __init__(self, name, physics, chemistry, maths):
        self.name = name
        self.physics = physics
        self.chemistry = chemistry
        self.maths = maths

    def avg_marks(self):
        return (self.physics + self.chemistry + self.maths) / 3


s1 = Student(
    input("Enter your name: "),
    int(input("Enter your physics marks: ")),
    int(input("Enter your chemistry marks: ")),
    int(input("Enter your maths marks: ")),
)
print("Average marks of", s1.name, "is:", s1.avg_marks())


# creating bank account with methods to debit, credit and get balance
class Account:
    def __init__(self, balance, acc):
        self.balance = balance
        self.acc = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "debited from your account")

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "credited to your account")

    def get_balance(self):
        return self.balance


acc1 = Account(50000, 555)
acc1.debit(5000)
acc1.credit(50000)
print("Your balance is:", acc1.balance, "your account number is:", acc1.acc)

# class:named employee, attr:role,department,salary, method:showDetails()
class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print(
 "role =", self.role,"\ndepartment =",self.department, 
 "\nsalary =", self.salary,)
        
# inherit properties from Employee, class:named Engineer, attr:name,age 
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","60,000")

eng1 = Engineer("Shraddha",20)
eng1.showDetails()
print(eng1.name)

# create class:Order, attr:item & price, use __gt__ dunder function
class Order:
    def __init__(self,items,price):
        self.items=items
        self.price=price

    def __gt__(order1,order2):
        return order1.price > order2.price


order1=Order("shoes",2500)
order2=Order("purse",4000)
print(order1 > order2)      # false
