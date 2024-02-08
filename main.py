# A dictionary with all the corresponding letters/numbers and their morse code
morse_dict = {
    "A": "-.",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}

# Get the user's input into morse code
text = input("Normal text: ")

# Check if there are symbols that are not in the international morse code
if not text.replace(" ", "").isalnum():
    print("Please use only letters and digits.")
else:
    print("Morse code: ", end="")
    for char in text:
        # Check if the char is a letter
        if char.isalpha():
            char = char.upper()
            print(morse_dict[char], end=" ")
        # Check if the char is a digit
        elif char.isdigit():
            print(morse_dict[char], end=" ")
        elif char.isspace():
            print("    ", end="")


