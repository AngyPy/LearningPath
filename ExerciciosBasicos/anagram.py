import string
import math

Text1 = " Anagrama "
print(f'{Text1:*^50}')

Name = [str(input("Enter a name: "))]
Name = Name[0].lower()
Name = Name.replace(" ", "")
Name = Name.translate(str.maketrans('', '', string.punctuation))

def create_anagram(name):
    anagram = name[::-1]
    return anagram

print(f"The anagram of {Name} is {create_anagram(Name)}")
