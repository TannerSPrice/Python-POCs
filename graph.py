# complex graph that shows up in console and makes different lines and colors when you edit them

import turtle
turtle.bgcolor("black")

#squary = turtle.Turtle()
#squary.speed(100)
#squary.pencolor("blue")
#for i in range(400):
 #   squary.forward(i)
 #   squary.right(91)
    

#second_squary = turtle.Turtle()
#second_squary.speed(100)
#second_squary.pencolor("red")
#for i in range(400):
#    second_squary.forward(i)
#    second_squary.left(91)

#third_spiral = turtle.Turtle()
#third_spiral.speed(100)
#third_spiral.pencolor("lime")
#for i in range(10):
#    third_spiral.forward(i)
#    third_spiral.right(91)

# circle
circle = turtle.Turtle()
circle.speed(100)
#circle.pencolor("yellow")
for i in range(400):
    circle.up()
    #circle.goto(0, -150)
    circle.down()
    circle.pencolor("yellow")
    circle.circle(150)
    
