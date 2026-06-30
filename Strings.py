# Indexing
str = "Arhama"
print(str[0])

# Slicing
str = "Arhama_Siddiqui"
print(str[6:14])  # same as [6:15] doesnt print end letter

# String function
str = "i am studying python"
print(str.endswith("on"))  # True
print(str.capitalize())  # Capitalize first letter
print(str.replace("python", "idk"))  # replaces old with new
print(str.find("p"))  # return index location
print(str.count("am"))  # how many times this word exist
