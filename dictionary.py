# make the dictionary
dict = {
    "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0,
    "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0,
    "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0,
    "v": 0, "w": 0, "x": 0, "y": 0, "z": 0, "+": 0, "-": 0,
    "/": 0, "*": 0, "%": 0, "=": 0, "(": 0, ")": 0, "^": 0,
    "!": 0, " ": 0, "0": 0, "1": 0, "2": 0, "3": 0, "4": 0,
    "5": 0, "6": 0, "7": 0, "8": 0, "9": 0
}
# var to be processed
myVar = "answer = (124.3866*9123.7835687)/56. This is my equation," + \
    " it can be long. It can take several lines on your screen."

# check each char if in dictionary increment the value for the ocurance
# lower to aviod error due to case
for char in myVar.lower():
    if char in dict:
        dict[char] += 1
    else:
        print("Error: invalid char " + char)

print("Dictonary of the equation")
# print the dictionary entry by entry
for x in dict:
    print (x, ":", dict[x])
