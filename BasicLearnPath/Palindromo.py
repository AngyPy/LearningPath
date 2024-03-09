import string

# Ask the user for a phrase
Phrase = str(input("Enter a phrase: "))

# Remove the spaces
replace = Phrase.replace(" ", "")

# Remove the punctuation
replace = replace.translate(str.maketrans('', '', string.punctuation))

# Convert to lowercase
lower = replace.lower()

# Reverse the string
invert = lower[::-1]

# Check if it's a palindrome
if lower == invert:
    print("It's a palindrome")
else:
    print("It's not a palindrome")