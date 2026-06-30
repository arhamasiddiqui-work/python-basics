# Loops(repeat instructions)

# while loop
i = 1  # initialize
while i <= 5:  # Stopping Condition
    print("hello world", i)
    i += 1  # Updation
print("loop ended")

i = 1  # initialize
while i <= 5:  # Stopping Condition
    print(i)
    if i == 4:
        break  # breaks/stops the loop
    i += 1  # Updation

i = 0  # initialize
while i <= 5:  # Stopping Condition
    if i == 4:
        continue  # skips the loop
    print(i)
    i += 1  # Updation


# for loop
list = [1, 2, 3, 4]
for val in list:
    print(val)

tup = (1, 2, 3, 4, 5)
for num in tup:
    print(num)

str = "Arhama"
for char in str:
    print(char)
else:
    print("END")

# range returns sequence of number, range(start?,stop,step?)

for index in range(10):  # range(stop)
    print(index)

for index in range(1, 10):  # range(start,stop)
    print(index)

for index in range(2, 10, 2):  # range(start,stop,step(update))
    print(index)

multiplication = int(input("enter number : "))
for i in range(1, 11):
    print(multiplication * i)

for i in range(100):
    pass  # leaving it empty for future code, it's null
