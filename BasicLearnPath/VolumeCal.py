
####Volume calculator for different shapes

#"This Python script is a simple volume calculator for various geometric shapes. 
# It provides a text-based user interface where the user can select the shape they want to 
# calculate the volume for. The shapes supported are:
#
#   1-  Cylinder
#   2-  Sphere
#   3-  Cone
#   4-  Cube
#   5-  Cuboid
#   6-  Triangular Prism
#   7-  Rectangular Prism
#   8-  Pyramid
#
#The user is prompted to enter the number corresponding to the shape they want to calculate
# the volume for. Depending on the shape selected, 
# the user is then asked to input the necessary dimensions (like radius, height, length, width)
# for that shape. The script then calculates and prints the volume of the selected shape.
#
#If the user enters "9", the script prints "Goodbye!" and ends.
#
#The script uses the math module for the mathematical constant pi (math.pi) 
# and the string module to remove punctuation from the user's input. 
# The script also includes some debugging print statements."

import math


#Introduction

Shapes = ("\n1. Cylinder \n2. Sphere \n3. Cone \n4. Cube \n5. Cuboid \n6." +
      "Triangular Prism \n7. Rectangular Prism \n8. Pyramid \n9. Exit \n")
TOption = ("Enter the number of the shape you want to calculate the volume for: ")


print("\n\n Volume Calculator")
print(f'\nThe shapes supported are: \n {Shapes}')

#Input for the shape
input = input(TOption)



             
#Cylinder
if input in [1]:
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    volume = math.pi * radius ** 2 * height
    print("The volume of the cylinder is", volume)
    
    
#Sphere
elif input in [2]:
    radius = float(input("Enter the radius of the sphere: "))
    volume = 4/3 * math.pi * radius ** 3
    print("The volume of the sphere is", volume)

#Cone
elif input in [3]:
    radius = float(input("Enter the radius of the cone: "))
    height = float(input("Enter the height of the cone: "))
    volume = 1/3 * math.pi * radius ** 2 * height
    print("The volume of the cone is", volume)
    
#Cube
elif input in [4]:
    side = float(input("Enter the side length of the cube: "))
    volume = side ** 3
    print("The volume of the cube is", volume)

#Cuboid
elif input in [5]:
    length = float(input("Enter the length of the cuboid: "))
    width = float(input("Enter the width of the cuboid: "))
    height = float(input("Enter the height of the cuboid: "))
    volume = length * width * height
    print("The volume of the cuboid is", volume)
    
#Triangular Prism
elif input in [6]:
    length = float(input("Enter the length of the triangular prism: "))
    width = float(input("Enter the width of the triangular prism: "))
    height = float(input("Enter the height of the triangular prism: "))
    volume = 1/2 * length * width * height
    print("The volume of the triangular prism is", volume)  

#Rectangular Prism
elif input in [7]:
    length = float(input("Enter the length of the rectangular prism: "))
    width = float(input("Enter the width of the rectangular prism: "))
    height = float(input("Enter the height of the rectangular prism: "))
    volume = length * width * height
    print("The volume of the rectangular prism is", volume) 

#Pyramid
elif input in [8]:
    length = float(input("Enter the length of the pyramid: "))
    width = float(input("Enter the width of the pyramid: "))
    height = float(input("Enter the height of the pyramid: "))
    volume = 1/3 * length * width * height
    print("The volume of the pyramid is", volume)   

#Exit
elif input in [9]:
    print("Goodbye!")
    
