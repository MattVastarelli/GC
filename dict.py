
dict = {
    "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,"i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0,
    "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,"y": 0, "z": 0, "+": 0, "-": 0,
    "/": 0, "*": 0,"%": 0, "=": 0, "(": 0, ")": 0, "^": 0, "!": 0, " ": 0, "0": 0, "1": 0,"2": 0, "3": 0, "4": 0,
    "5": 0, "6": 0, "7": 0, "8": 0, "9": 0
}

myVar = "answer = (124.3866*9123.7835687)/56. This is my equation, it can be long. It can take " + \
        "several lines on your screen."

for char in myVar.lower():
    if char == "a":
        dict["a"] += 1
    elif char == "b":
        dict["b"] += 1
    elif char == "c":
        dict["c"] += 1
    elif char == "d":
        dict["d"] += 1
    elif char == "e":
        dict["e"] += 1
    elif char == "f":
        dict["f"] += 1
    elif char == "g":
        dict["g"] += 1
    elif char == "h":
        dict["h"] += 1
    elif char == "i":
        dict["i"] += 1
    elif char == "j":
        dict["j"] += 1
    elif char == "k":
        dict["k"] += 1
    elif char == "l":
        dict["l"] += 1
    elif char == "m":
        dict["m"] += 1
    elif char == "n":
        dict["n"] += 1
    elif char == "o":
        dict["o"] += 1
    elif char == "p":
        dict["p"] += 1
    elif char == "q":
        dict["q"] += 1
    elif char == "r":
        dict["r"] += 1
    elif char == "s":
        dict["s"] += 1
    elif char == "t":
        dict["t"] += 1
    elif char == "u":
        dict["u"] += 1
    elif char == "v":
        dict["v"] += 1
    elif char == "w":
        dict["w"] += 1
    elif char == "x":
        dict["x"] += 1
    elif char == "y":
        dict["y"] += 1
    elif char == "z":
        dict["z"] += 1
    elif char == "0":
        dict["0"] += 1
    elif char == "1":
        dict["1"] += 1
    elif char == "2":
        dict["2"] += 1
    elif char == "3":
        dict["3"] += 1
    elif char == "4":
        dict["4"] += 1
    elif char == "5":
        dict["5"] += 1
    elif char == "6":
        dict["6"] += 1
    elif char == "7":
        dict["7"] += 1
    elif char == "8":
        dict["8"] += 1
    elif char == "9":
        dict["9"] += 1
    elif char == " ":
        dict[" "] += 1
    elif char == "+":
        dict["+"] += 1
    elif char == "-":
        dict["-"] += 1
    elif char == "/":
        dict["/"] += 1
    elif char == "*":
        dict["*"] += 1
    elif char == "%":
        dict["%"] += 1
    elif char == "^":
        dict["^"] += 1
    elif char == "!":
        dict["!"] += 1
    elif char == "=":
        dict["="] += 1
    elif char == "(":
        dict["("] += 1
    elif char == ")":
        dict[")"] += 1
    else:
        print("Error: invalid char " + char)

print("Dictonary of the equation")

for x in dict:
    print (x, ":" ,dict[x])

