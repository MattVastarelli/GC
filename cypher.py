# Cypher as a dict
dict = {
    "a": "z", "b": "y", "c": "x", "d": "w", "e": "v", "f": "u", "g": "t",
    "h": "s", "i": "r", "j": "q", "k": "p", "l": "o", "m": "n", "n": "m",
    "o": "l", "p": "k", "q": "j", "r": "i", "s": "h", "t": "g", "u": "f",
    "v": "e", "w": "d", "x": "c", "y": "b", "z": "a",
}

# input string
varInput = "There is something infantile in the presumption that" + \
    "somebody else has a responsibility to give your life meaning " + \
    "and point… The truly adult view, by contrast, is that our " + \
    "life is as meaningful, as full and as wonderful as we choose to make it."
# new string for substution cypher
subCypher = ""

print("Input prior to cypher: ", varInput)

# substution cypher
# lower to aviod error due to case
for char in varInput.lower():
    if char in dict:
        subCypher += dict[char]
    else:
        subCypher += char

print("\nSubstution Cyber: ", subCypher)

# transpostion cypher
