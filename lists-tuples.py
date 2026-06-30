# LISTS (arrays), lists are mutable(changeable),  elements of diff types can be stored in python,

student = ["Random", 17, "Pechs"]
print(student[0])
student[0] = "Arhama"
print(student[0])

#  slicing (same as string)
list = ["grocery", "working", "budget"]
print(list[0:2])

# list function
list = [3, 2, 1]
list.append(0)  # adding element
list.sort()  # sorts in ascending order
list.sort(reverse=True)  # sorts in descending order
list.reverse()  # reverse the items
list.insert(0, 4)  # add element at index
list.pop(0)  # removes element at index
list.remove(3)  # remove specific element
print(list)


# TUPLES, tuples are immutable (non-changeable), elements of diff types can be stored in python
student = (
    "Random",
    17,
    "Pechs",
)
print(student[0])

#  slicing (same as string)
tup = ("grocery", "working", "budget")
print(tup[0:2])

# tuples function
tup = (3, 2, 1)
print(tup.index(2))  # how many times this element exist
print(tup.count(2))  # how many times this element exist


# Practice Question
list1 = [
    input("enter your 1 fav movie : "),
    input("enter your 2 fav movie : "),
    input("enter your 3 fav movie : "),
]
print("Wohoo! nice moviesss", list1)

list = [1, 2, 3, 2, 1]  # palindrome(same if we read from both way)
copy_list = list.copy()
copy_list.reverse()

if copy_list == list:
    print("Palindrome")
else:
    print("Not same")
