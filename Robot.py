# for random
from random import randint

print("Day 1 Program")
counter = 0
var1 = ""
stringList = ["Thank you for sharing ", "That’s interesting ", "Good to hear "]
inFile = open("dataFile.txt")
outFile = open("outFile.txt", "w")

print("Into python part")
# while till quit
print("while loop")
while var1 != "quit":
    var1 = input("enter input or quit to quit: ")

    if var1 == "python":
        print("Gen Cyber")
    else:
        print(var1)

# For 5
print("for loop")
for i in range(5):
    var1 = input("enter input: ")
    counter += 1
    print(var1, "Counter: ", counter)

print("Advanced python part")

# while till quit
print("while loop")
while var1 != "quit":
    var1 = input("enter input or quit to quit: ")
    print(stringList[randint(0, 2)], var1)

# file stuff
# read
# strip
print("Reading from file")
with open("dataFile.txt") as f:
    var1 = f.readlines()
    var1 = [x.strip() for x in var1]
# reset counter
counter = 0

# print convo
print("print convo")
for str in var1:
    print(stringList[randint(0, 2)], var1[counter])
    counter += 1

counter = 0

# print to file
print("print to file")
# hold line
newLine = ""
# hold more than one line
newParagraph = ""
for str in var1:
    newLine = stringList[randint(0, 2)] + var1[counter]
    counter += 1
    newParagraph += newLine + "\n"

# write to the file
outFile.write(newParagraph)
# close the files
inFile.close()
outFile.close()
