#  Mini Project

# guess the number: (loops logic)
import random           #helps in generating random number,characters
target=random.randint(1,100)            # randint = integer

while True:
    userNum=input("Guess the Number or Quit(Q) : ")
    if(userNum == "Q"):
        break
    userNum= int(userNum)
    if(userNum == target):
        print("Success : Correct Guess!")
        break
    elif(userNum<target):
       print("Take a bigger Guess...")
    else:
       print("Take a smaller Guess..")

print("---GAME OVER---")

# random password generator:
import random
import string                    # all characters        

charVal = string.ascii_letters + string.digits + string.punctuation

# by list way: 1 line code
password="".join([random.choice(charVal) for i in range(10)])
print(password)

# normal way:  3 line code
# password=""
# for i in range(10):
#     password += random.choice(charVal)

print("Your random password is : ",password)   