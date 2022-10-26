from turtle import *

print("Enter the number two")
num = int(input("num : "))
if num == 2:
    for i in range(0, 4):
        forward(150)
        left(90)
    for i in range(0, 3):
        backward(150)
        right(90)
    backward(300)
    left(90)
    for i in range(0, 2):
        forward(150)
        right(90)
    penup()

    forward(300)

    pendown()

    right(90)
    forward(150)
    right(90)
    forward(150)
    right(45)
    forward(212)
    right(90)
    forward(210)
    right(90)
    forward(212)
    right(90)
    forward(212)
else:
    print("You didn't enter the number two")
    done()

# Python program to user input pattern
# using Turtle Programming
import turtle  # Outside_In
# import turtle
# import time
# import random
#
# print("This program draws shapes based on the number you enter in a uniform pattern.")
# num_str = input("Enter the side number of the shape you want to draw: ")
# if num_str.isdigit():
#     squares = int(num_str)
#
# angle = 180 - 180 * (squares - 2) / squares
#
# turtle.up
#
# x = 0
# y = 0
# turtle.setpos(x, y)
#
# numshapes = 8
# for x in range(numshapes):
#     turtle.color(random.random(), random.random(), random.random())
#     x += 5
#     y += 5
#     turtle.forward(x)
#     turtle.left(y)
#     for i in range(squares):
#         turtle.begin_fill()
#         turtle.down()
#         turtle.forward(40)
#         turtle.left(angle)
#         turtle.forward(40)
#         print(turtle.pos())
#         turtle.up()
#         turtle.end_fill()
#
# time.sleep(11)
# turtle.end()

