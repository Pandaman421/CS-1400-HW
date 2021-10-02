'''
Project Name:
Author:
Due Date: YYYY-MM-DD
Course: CS1400-zzz

Put your description here, lessons learned here, and any other information
someone using your program would need to know to make it run.
'''
import turtle
from math import *
import random

def rectangle(turtle, x = 0, y = 0, width = 50, height = 30, rotation = 0, color = 'white'):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(rotation)
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.right(rotation)
    
def triangle(turtle, x = 0, y = 0, size = 50, rotation = 0, color = 'white'):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(rotation)
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.right(rotation)
    
def circle(turtle, x = 0, y = 0, diameter = 50, rotation = 0, color = 'white'):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(rotation)
    for i in range(360):
        turtle.forward(diameter/115)
        turtle.left(1)
    #here it's more complex, I'm gonna use this function online I found for drawing a heart on a graph.
    #I define it to use time = time, I'm changing variable to change the coordinates for the heart
    # I might switch this to it's own function later.
    turtle.right(rotation)
    turtle.penup()
    
def heart (turtle, x = 0, y = 0, size = 50, rotation = 0, color = 'pink'):
    turtle.penup()
    time = 0
    turtle.goto((16*(sin(time))**3)*size+x, ((13*cos(time)-5*cos(2*time)-2*cos(3*time)-cos(4*time))*size+y))
    turtle.pendown()
    for i in range(200):
        time = (2*pi/200)*i
        turtle.goto((16*(sin(time))**3)*size+x, ((13*cos(time)-5*cos(2*time)-2*cos(3*time)-cos(4*time))*size+y))

def tree(turtle, x = 0, y = 0, size = 10):
    size = size*0.1
    turtle.color('brown', 'brown')
    turtle.begin_fill()
    rectangle(turtle, x, y, 20*size, 90*size)
    triangle(turtle, 20*size+x, y, 10*size)
    rectangle(turtle, 20*size+x, y, 8*size, 30*size, 20)
    triangle(turtle, x, y, 10*size, 120)
    turtle.end_fill()
    turtle.begin_fill()
    rectangle(turtle, x, y, 8*size, -30*size, 160)
    turtle.end_fill()
    turtle.color('green', 'green')
    turtle.begin_fill()
    circle(turtle, 10*size+x, 70*size+y, 50*size)
    turtle.end_fill()
    turtle.begin_fill()
    circle(turtle, -10*size+x, 60*size+y, 40*size)
    turtle.end_fill()
    turtle.begin_fill()
    circle(turtle, 30*size+x, 60*size+y, 40*size)
    turtle.penup()
    turtle.end_fill()
    
def main():
    t = turtle.Turtle()
    turtle.tracer(0, 0)
    for i in range(100):
        tree(t, random.randrange(-500, 500), 400-i*8, 10)
    tree(t, 0, -50, 20)
    '''
    try:
        pass
    except ValueError:
        print('Width and height must be positive integers.')
        return

    if width < 1 or height < 1:
        print('Width and height must be positive integers.')
        return

    # (2) replace pass with your code
    pass
'''
if __name__ == "__main__":
    main()
