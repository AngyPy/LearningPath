import math
import string

print("1 - Area of the circle\n 2 - Area of the triangle\n" +
    "3 - Area of the square\n 4 - Exit the program\n")

option = str(input("Choose an option: "))
replace = option.replace(" ", "")
replace = str(replace.translate(str.maketrans('', '', string.punctuation)))
option = option.lower()

if replace in ["1", "areaofthecircle"]:
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    print(f"The area of the circle is {area:.2f}")
    
elif replace in ["2", "areaofthetriangle"]:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = (base * height) / 2
    print(f"The area of the triangle is {area:.2f}")
    
elif replace in ["3", "areaofthesquare"]:
    side = float(input("Enter the side of the square: "))
    area = side ** 2
    print(f"The area of the square is {area:.2f}")
    
elif replace in ["4", "exit"]:
    print("Exiting the program...")
    exit()