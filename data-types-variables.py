"""print("Hello World!", "Learning Python basics :)")"""

# Data types & variables
age = 20  #     -> integer
price = 5.99  # -   > Float
# others data types are same as js
print(type(age))

# taking input from user,  input is string we have to typecaste it
name = input("enter your name: ")
age = int(input("enter your age :"))
marks = float(input("Your marks are:"))

print("Welcome", name)
print("Your age is", age)
print("marks", marks)

# if-elif-else conditional statements (multiple line)
marks = int(input("marks : "))
if marks >= 90:
    print("A+")  # indentation: proper spacing is v.imp
elif marks >= 80:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("F")

# Ternary Operators
# if-else   (single line)
food = input("Guess my fav food : ")
eat = "Yes" if food == "Lasagne" else "no"
print(eat)

food = input("food : ")
print("sweet") if food == "cake" or food == "cookie" else print("not sweet")

# Clever if statement
age = int(input("age : "))
vote = ("yes", "no")[age < 18]
print(vote)

# Logical Operator:
#   NOT = input True - Output False (reversed)
#   AND = input True and False - Output False (if both r equal then will give true, else false)
#   OR = input True and False - Output True (if anyone is true then will give true)

Not = print(not False)
And = print(True and False)
Or = print(True or False)

# Type Conversion (automatically)
a = 2
b = 1.99
sum = a + b
print(type(sum))

# Type Casting (manually)
a = int("2")
b = 1.99
sum = a + b
print(type(sum))


# Practice Question:
num = int(input("enter a number : "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
