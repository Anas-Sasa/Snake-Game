from turtle import Turtle
import random


class Snake:
    def __init__(self, color, length, speed):
        
        self.turtles = []
        self.color = color
        self.length = length
        self.speed = speed
        self.creat_snake()
        self.head = self.turtles[-1]

    def creat_snake(self):
        
        snake_position = (self.length * 20) -20

        for _ in range(self.length):

            t = Turtle("square")
            t.penup()
            t.color(self.color)
            t.goto(x= -snake_position, y=0)
            self.turtles.append(t)

    def move(self, window):

        for i in range( len(self.turtles) -1 ):

            self.turtles[i].goto( self.turtles[ i + 1 ].pos() )

        self.head.forward(self.speed)
        window.update()

    def hide_snake(self):

        for turtle in self.turtles:
            turtle.hideturtle()

    def snake_extend(self):
        
        t = Turtle("square")
        t.penup()
        t.color(self.color)
        self.turtles.insert(0, t)

    def down(self):

        if self.head.heading() != 90:
            self.head.setheading(270)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)





        