# This program draws the letters A, N, G, Y using turtle graphics
# NOT WORKING YET... not sure why... I think it's because the turtle is not drawing the 
# letters in the right place
# I will try to fix it later

import turtle

def draw_A(turtle, height):
    print("Drawing A")
    turtle.color("purple")
    turtle.left(75)
    turtle.forward(height)
    turtle.right(150)
    turtle.forward(height)
    turtle.backward(height/2)
    turtle.right(105)
    turtle.forward(height/3)
    turtle.backward(height/3)
    turtle.left(105)
    turtle.backward(height/2)

def draw_N(turtle, height):
    print("Drawing N")
    turtle.color("hotpink")
    turtle.left(90)
    turtle.forward(height)
    turtle.right(150)
    turtle.forward(height)
    turtle.left(150)
    turtle.forward(height)
    turtle.right(90)

def draw_G(turtle, height):
    print("Drawing G")
    turtle.color("purple")
    turtle.forward(height/2)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(height/2)
    turtle.right(90)
    turtle.forward(height/2)
    turtle.right(90)
    turtle.forward(height/2)

def draw_Y(turtle, height):
    print("Drawing Y")
    turtle.color("hotpink")
    turtle.left(30)
    turtle.forward(height)
    turtle.backward(height/2)
    turtle.right(60)
    turtle.forward(height/2)
    turtle.backward(height/2)
    turtle.left(30)

window = turtle.Screen()
window.bgcolor("lightblue")
pen = turtle.Turtle()
pen.pensize(5)

draw_A(pen, 100)
pen.penup()
pen.forward(120)
pen.pendown()

draw_N(pen, 100)
pen.penup()
pen.forward(120)
pen.pendown()

draw_G(pen, 100)
pen.penup()
pen.forward(120)
pen.pendown()

draw_Y(pen, 100)

window.mainloop()