from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, color):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.color(color)
        self.shape("circle")
        self.shapesize(0.5, 0.5)

    def apear_food(self):
        x_cor = random.randint(-470, 470)
        y_cor = random.randint(-370, 370)
        self.showturtle()
        self.goto(x= x_cor, y= y_cor)
        
    def hide_food(self):
        self.hideturtle()