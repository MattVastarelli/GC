#input string
varInput = "There is something infantile in the presumption that somebody else has a responsibility to give " + \
           "your life meaning and point… The truly adult view, by contrast, is that our life is as meaningful, " + \
           "as full and as wonderful as we choose to make it."
# new string for substution cypher
subCypher = ""

print("Input prior to cypher: ", varInput)

#substution cypher
for char in varInput.lower():#lower to aviod error due to case
    if char == "a":
        subCypher += "z"
    elif char == "b":
        subCypher += "y"
    elif char == "c":
        subCypher += "x"
    elif char == "d":
        subCypher += "w"
    elif char == "e":
        subCypher += "v"
    elif char == "f":
        subCypher += "u"
    elif char == "g":
        subCypher += "t"
    elif char == "h":
        subCypher += "s"
    elif char == "i":
        subCypher += "r"
    elif char == "j":
        subCypher += "q"
    elif char == "k":
        subCypher += "p"
    elif char == "l":
        subCypher += "o"
    elif char == "m":
        subCypher += "n"
    elif char == "n":
        subCypher += "m"
    elif char == "o":
        subCypher += "l"
    elif char == "p":
        subCypher += "k"
    elif char == "q":
        subCypher += "j"
    elif char == "r":
        subCypher += "i"
    elif char == "s":
        subCypher += "h"
    elif char == "t":
        subCypher += "g"
    elif char == "u":
        subCypher += "f"
    elif char == "v":
        subCypher += "e"
    elif char == "w":
        subCypher += "d"
    elif char == "x":
        subCypher += "c"
    elif char == "y":
        subCypher += "b"
    elif char == "z":
        subCypher += "a"
    else:
        subCypher += char

print("\nSubstution Cyber: ", subCypher)

#transpostion cypher

