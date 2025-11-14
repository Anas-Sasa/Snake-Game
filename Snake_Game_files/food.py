"""
food.py

Defines the Food class for a simple collectible item using the turtle graphics library.

Classes:
    Food -- Subclasses turtle.Turtle to create a small circular food item that can
            appear at random positions on the screen or be hidden.

Usage:
    from food import Food
    snack = Food(color="red")
    snack.apear_food()
    snack.hide_food()
"""


# Import Turtle for drawing and random for positioning the food randomly on screen
from turtle import Turtle
import random


class Food(Turtle):
    """
    A small circular food item for a game board.

    Parameters
    ----------
    color : str
        Color used to draw the food.
    """

    def __init__(self, color):
        # Initialize the parent Turtle class
        super().__init__()

        # Start hidden because food should appear on demand
        self.hideturtle()

        # Lift the pen so moving the food does not draw lines on the canvas
        self.penup()

        # Set the visual color of the food
        self.color(color)

        # Use a circle shape to represent the food
        self.shape("circle")

        # Make the food smaller than default so it looks like a pellet
        self.shapesize(0.5, 0.5)

    def apear_food(self):
        """
        Show the food at a random position within screen bounds.

        Chooses a random x and y coordinate inside predefined ranges,
        moves the food there, and makes it visible.
        """
        # Choose random coordinates inside a typical play area
        x_cor = random.randint(-470, 470)
        y_cor = random.randint(-370, 370)

        # Make the food visible and move it to the chosen coordinates
        self.showturtle()
        self.goto(x= x_cor, y= y_cor)

    def hide_food(self):
        """
        Hide the food from the screen without moving it.
        """
        self.hideturtle()
