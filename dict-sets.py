# Dictionary (Objects), they are mutable(changeable), key:value pairs

info = {
    "name": "Guess",
    "age": 0,
    "is_adult": True,
    "activities": ["learning", "working", "building"],
    "topic": ("dictionary", "set"),
}

info["name"] = "melissa"  # accessing & changingindividual values
info["newName"] = "Random"
print(
    info["surname"]
)  # will throw error bc this key doesnt exist thats why use .get method


# nested
student = {
    "name": "melissa",
    "subjects": {
        "chem": 50,
        "maths": 60,
    },
}
print(student["subjects"]["maths"])

#   Dictionary methods
info = {
    "name": "Arishah",
    "age": 19,
}
print(list(info.keys()))  # returns the keys
print(list(info.values()))  # returns the values
print(info.items())  # return key:val pairs as tuples
print(info.get("info1"))  # returns key according to val,no error
info.update({"city": "Karachi"})  # adding/updating a new key:val pair
print(info)

emptydict = {}  # For dict
emptyset = set()  # For set


# Sets (Collection of unordered items),sets r mutable(changeable) while set element r immutable & unique, it ignore duplicate values
nums = {1, 2, 3, 4, "hello", "duplicate", "duplicate"}
print(nums)

# Sets method
collection = {1, 2, 3, 4}
collection.add(5)  # adds a element in collection
collection.remove(5)  # remove a element from collection
collection.clear()  # empties the set
collection.pop()  # remove random value
print(collection)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # combines both set & return new

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.intersection(set2))  # combines common val & return new

# Pratice Question:
dict = {
    "cat": "Cats are popular, independent, and affectionate pets",
    "Husky": [
        "spirited and athletic working dog",
        "incredible Arctic working dogs bred",
    ],
}
print(dict)


Subjects = {"javascript", "python", "java", "C++", "C", "C++", "python"}
print(len(Subjects))


marks = {}
x = int(input("enter physics: "))
marks.update({"phys": x})
x = int(input("enter maths: "))
marks.update({"maths": x})
print(marks)
