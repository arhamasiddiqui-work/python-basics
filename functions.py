# Functions (to make redundancy/repetition low)


def calcSum(a, b):
    sum = a + b
    print(sum)


calcSum(2, 3)
calcSum(3, 3)


def calcAvg(a, b, c):
    avg = a + b + c / 3
    print(avg)


calcAvg(2, 2, 2)

nums = [1, 2, 3, 4]
cities = ["karachi", "lahore", "islamabad"]


def length(list):
    print(len(list))


length(nums)
length(cities)


# function usd -> pkr
def converter(usd):
    pkr = usd * 278
    print(usd, "USD =", pkr, "PKR")


converter(1)


# Recursion(WHEN A FUNCTION CALLS ITSELF REPEATEDLY), callstack,loop
def show(n):
    if n == 0:  # stopping/base case
        return
    print(n)
    show(n - 1)


show(5)


# factorial: 4! (four factorial) = 4 * 3 * 2 * 1 = 24
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return factorial(n - 1) * n


print(factorial(4))


def print_list(list, index=0):
    if index == len(list):
        return
    print(list[index])
    print_list(list, index + 1)


cities = ["karachi", "lahore", "islamabad"]
print_list(cities)
