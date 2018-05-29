#  NSA - GenCyber
Solutions to the assigned challenges 
#### About
GenCyber is hosted by UNHcFREG and the engineering college to teach high school students

interested in digital forensics and security. Topics include web applications, ethical hacking, 

drone forensics, and more.
#### Table of Contents 
* Problems
	* 	[Lab 1 Assignment](#lab-1-assignment)
	* 	[Lab 2 Assignment](#lab-2-assignment) 
	* 	[Lab 3 Assignment](#lab-3-assignment)
* Why it works
	* [Lab 1 Info/Help](#lab-1-info/help)
	* [Lab 2 Info/Help](#lab-2-info/help)
	* [Lab 3 Info/Help](#lab-3-info/help)

#### Problems

##### Lab 1 Assignment
Create a project called “1 Echo”. Create a python program called “echo” in this
project. 

You will see it in the “1 Echo” folder, called echo.py
Using the print() statement and working with data, 

have your program to write  a message to the console.
Now make the following changes/additional to your program:

1. Add a text variable to your program and print that, too.
2. Add a numeric variable, do you remember how to turn it into a string for output? Print the number as well.
3. Do a calculation using a math function I did not discuss – be ready to share this with the
	class. You will need to import this from the math library. (If you never programmed before,
	you can just use an equation using + - * / % or ^).
4. Use the random number generator in the random library (do you know how to import this?)
	to include a random number in your program. Print it out with a label identifying it. Use it in
	a calculation. Example: random.randint(0,20)
    
 [Solution](https://github.com/MattVastarelli/GC/blob/master/lab1.py)

##### Lab 2 Assignment
Create a project called “2 Robot”. Create a python program called “robot” in this
project will.

1. Use the input() function to show a prompt and then accept input from the user into a
	variable. Start with a single word or number. Then go on to a full sentence. Sentences
	separated by enter keys or newlines, will be processed separately. You need a loop for
	that(not covered yet – advanced students use while or for loop – which works better here?)
	Print out the data that was entered.
2. Use an if statement to decide what to do based on input.
	a. You can print a special message if a certain word is entered, otherwise echo the
	input.
	b. If you wrote a loop, ask user to enter ‘quit’ (or ‘$’) to exit your program and write an
	if statement that breaks the loop when it is input.

3. Write a for loop to continue accepting input five times. Each time, echo the input with your
	count. Don’t forget to have a counter and increment it inside the loop.
4. Now use a while loop and continue to accept input until the user enters ‘quit’ (or ‘exit’ or ‘$’
	if you prefer). Hit the red square to the left of the console window at the bottom of Pycharm
	to terminate your program if it won’t stop.

5. Advanced students

	a. Create a simple list of strings and randomly pick a response to input. For Example:
	“Thank you for sharing.” Try to use sentences that will seem logical no matter what
	is entered. “That’s interesting.”, etc.
    
	b. Now add a word from the input to your sentence (the easiest is to pull off the last
	word or the first one from the entry and put it at the end of your message). For
	example: print(“I am interested in “ + lastWord). See if you can make your robot
	sound human.
    
	c. Using python functions, input from a file. Now use the file as input to your robot
	program. How does it look?
    
	d. Need more: create a file for output and call it myOutput.txt. Put a heading in the
	file, then put the conversation into the file. See how nice you can make it look. Use
	the end= feature to make paragraphs.
    
     [Solution](https://github.com/MattVastarelli/GC/blob/master/Robot.py)
    
 ##### Lab 3 Assignment
 
Create a python program called “countNumbers” in this project by clicking File/New/Python
Program. 

Create a program to count the number of each numerical digit (0 to 9) in a mathematical equation text.
You can add a text to a file by creating a new string variable that contains your text or take it as input.
myVar = “answer = (124.3866*9123.7835687)/56. This is my equation, it can be long. It can take “ +
“several lines on your screen.”
 FYI The + is the concatenation symbol, we have been using it in the print() statements, it works the
same way in an assignment statement.
You will need a dictionary of the numerical characters with a number for the count (start with zero for
every digit – see my program for the syntax).
Create a for loop to go through the equation and count how many of each digit is in your equation. I will
demonstrate how to do this for letters and share the code to my google drive.
Now print out the resulting table. Don’t forget to print several items per line with comma and space
between them, so your table is compact.

 [Solution](https://github.com/MattVastarelli/GC/blob/master/dictionary.py)
     
#### Why it works

##### Lab 1 Info/Help
The libraries that need to be accessed through the import statement.
```python
import math
import random
````

The  variable assigned to textvar is a string and to print all that is needed is to place in the () of a print() statement. 
```python
textvar = "text Var"
print("Text: ", textvar)
```
The same thing goes of a number.
```python
snumVar = 6
print("Number: ", numVar)
```
This prints the original number  followed by its factorial. The factorial is done by accessing the math library as math is the object the various functions i.e. factorial, square root need to be referenced using the ".". The factorial is a function that takes input of a number in this case 6 and finds its factorial.
```python
print("Math function number: ", numVar, " factorial: ", math.factorial(numVar))
```
randNum receives a random integer between 0 and 20 from the output of the randint function where the first number in the () is the lowest and the second the highest. The print statement  shows the random number and then sums it with numVar or 6.
```python
randNum = random.randint(0,20)
print("Random number: ", randNum, " Plus Number var = ", randNum + numVar)
```

###### Take away
1. The print statement could do more than just print including math, calling a function.
2. libraries must be added via "import"
3. some times library functions require accessing the library by its name i.e. "Math" and its function by ".factorial" 

##### Lab 2 Info/Help
Files are opened using the open() function, this function will create a new file in the local directory if one of that name does not already exist. The open function allows a program to set the privileges of a file by passing it in along as a string with the file name, for basics write = "w" read = "r".
````python
inFile = open("dataFile.txt")
outFile = open("outFile.txt","w")
````
A while loop checks if its condition is true at the top of the loop before it executes thus input is taken that will print or quit depending on what is entered. 
```python
while var1 != "quit":
    var1 = input("enter input or quit to quit: ")

    if var1 == "python": print("Gen Cyber")
    else: print(var1)
```
For Loops execute their code for a set number of times, which is specified by the range() method or by the number of items in an element. 
```python
print("for loop")
for i in range(5):
    var1 = input("enter input: ")
    counter += 1
    print(var1,"Counter: ", counter)
```
Remember Indexes of start at 0
```python
while var1 != "quit":
    var1 = input("enter input or quit to quit: ")
    print(stringList[randint(0,2)], var1)
```
To read from a file for input you must read line by line using the readlines function. if you wish you may remove the white space using the strip function.
```python
with open("dataFile.txt") as f:
    var1 = f.readlines()# read
    var1 = [x.strip() for x in var1] #strip
```
Write to a file using the write function.
```python
outFile.write(newParagraph)
```
Always remember to close the file
````python
inFile.close()
outFile.close()
````
##### Lab 3 Info/Help
Dictionaries are structures that have a key in this case the letter and a value for this example the numbers. It should be noted that in dictionaries both the key and the value could be accessed.
```python
#make the dictionary
dict = {
    "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,"i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0,
    "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,"y": 0, "z": 0, "+": 0, "-": 0,
    "/": 0, "*": 0,"%": 0, "=": 0, "(": 0, ")": 0, "^": 0, "!": 0, " ": 0, "0": 0, "1": 0,"2": 0, "3": 0, "4": 0,
    "5": 0, "6": 0, "7": 0, "8": 0, "9": 0
}
```
Dictionaries are use full as they allow you to check the if an item is in the dictionary and modify its value.
```python
for char in myVar.lower():
    if char in dict:
        dict[char] += 1
    else:
        print("Error: invalid char " + char)
```
To print a dictionary you must print both the key and value of every element in the dictionary.
```python
for x in dict:
    print (x, ":" ,dict[x])
```

