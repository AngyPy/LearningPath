#Calc

import math
import string

print(" 1 - Addition\n 2 - Subtraction\n 3 - Multiplication\n 4 - Division\n" +
        "5 - Exponentiation\n 6 - Square Root\n 7 - Exit\n")

option = str(input("Choose an option: "))
replace = option.replace(" ", "")
replace = replace.translate(str.maketrans('', '', string.punctuation))
lower = replace.lower()
lower = option

if option in ["1", "addition", "+"]:
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    print("Result: ", n1 + n2)

elif option in ["2", "subtraction", "-"]:
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    print("Result: ", n1 - n2)

elif option in ["3", "multiplication", "*"]:
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    print("Result: ", n1 * n2)
    
elif option in ["4", "division", "/"]:
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    print("Result: ", n1 / n2)

elif option in ["5", "exponentiation", "**"]:
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    print("Result: ", n1 ** n2)

elif option in ["6", "squareroot"]:
    n1 = float(input("Enter the number: "))
    print("Result: ", math.sqrt(n1))
    
elif option in ["7", "exit"]:
    print("Exiting...") 