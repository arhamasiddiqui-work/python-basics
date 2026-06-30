# File I/O (read & over write data in a file)

# types of files:
# Textfiles:data in characters (e.g: .txt, .docx, .log, etc)
# Binaryfiles:data in otherformat(e.g: .mp4, .mov, .png, .jpeg, etc)

# characters:
# r -> read (default)
# w -> over write
# a -> append
# x -> create
# t -> text mode (default)
# b -> binary mode
# + -> read and write

# opening file by 2 ways:

f = open("text.txt", "r")  # 1st way
data = f.read()
print(data)
f.close()

with open("text.txt", "r") as f:  # 2nd way
    data = f.read()
    print(data)

#  READING FILES:
f = open("text.txt", "r")
data = f.read()  # reads entire file
print(data)
line1 = f.readline()  # reads one line at a time
print(line1)
f.close()


f = open("text.txt", "r+")  # read and write
f.write("reading & writing data")
f.close()

f = open("text.txt", "w+")  # read and over write
f.write("reading & writing data in a file")
f.close()

f = open("text.txt", "a+")  # read and append
f.write("\nreading & appending data in a file")
f.close()

#  OVERWRITING DATA IN A FILE:  (can create a new file if it doesn't exist)
f = open("sample.txt", "w")
f.write("I want to become a good programmer")
f.close()

#  APPENDING DATA IN FILE: (can create a new file if it doesn't exist)
f = open("sample.txt", "a")
f.write("\nI am currently learning Python")
f.close()

# OPENING FILE 'WITH' SYNTAX:

# READING FILES:
with open("text.txt", "r") as f:
    data = f.read()
    print(data)

#  OVERWRITING DATA IN A FILE:
with open("text.txt", "w") as f:
    f.write("I want to become a good programmer")

# DELETING FILES: (using OS module)
import os

os.remove("sample.txt")  # deletes the file

# PRACTICE QUESTIONS :
with open("practice.txt", "w") as f:
    data = f.write("Hi Everyone\nI am learning Python")

with open("practice.txt", "r") as f:
    data = f.read()
newdata = data.replace("Python", "Java")  # replacing Python with Java
print(newdata)

with open("practice.txt", "r") as f:
    data = f.read()
    if (
        data.find("learning") != -1
    ):  # checking if the word learning is present in the file or not
        print("Found")
    else:
        print("Not Found")
