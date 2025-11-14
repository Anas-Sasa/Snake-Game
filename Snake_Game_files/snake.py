"""
snake.py

Defines a simple Snake class for a snake game using turtle graphics.

The Snake class manages a list of Turtle segments that form the snake,
handles creation, movement, growth, hiding, and direction controls.

Usage:
    from snake import Snake
    snake = Snake(color="green", length=3, speed=20)
    snake.move(screen)
    snake.up()
"""


# Import Turtle to create and control the snake segments
from turtle import Turtle

class Snake:
    """
    Manage a snake composed of Turtle square segments.

    Parameters
    ----------
    color : str
        Color used for all snake segments.
    length : int
        Initial number of segments.
    speed : int
        Forward movement distance per step.
    """

    def __init__(self, color, length, speed):

        # List holding turtle segments from tail (index 0) to head (last index)
        self.turtles = []

        # Store configuration values
        self.color = color
        self.length = length
        self.speed = speed

        # Create the initial snake segments
        self.creat_snake()

        # Keep a direct reference to the head segment for movement and heading
        self.head = self.turtles[-1]

    def creat_snake(self):
        """
        reate initial snake segments spaced by 20 pixels."""

        # Calculate starting x offset so the snake extends to the right from origin
        snake_position = (self.length * 20) - 20

        # Create each segment as a square turtle and position them in a row
        for _ in range(self.length):

            t = Turtle("square")
            t.penup()           # don't draw lines when moving segments
            t.color(self.color) # set segment color
            t.goto(x= -snake_position, y=0)  # place segment

            self.turtles.append(t)


    def move(self, window):
        """
        Move the snake forward by making each segment follow the next one,
        then advancing the head by `self.speed`. The window is updated after move.
        """
       
        # Update positions from tail to the segment before the head
       
        for i in range(len(self.turtles) - 1):

            # Each segment takes the position of the segment in front of it
            self.turtles[i].goto(self.turtles[i + 1].pos())

        # Move the head forward by the configured speed
        self.head.forward(self.speed)

        # Refresh the screen to show the movement
        window.update()

    def hide_snake(self):
        """
        Hide all segments (useful when resetting or ending the game)."""

        for turtle in self.turtles:
            turtle.hideturtle()

    def snake_extend(self):
        """
        Add a new segment at the tail end.

        Creates a new Turtle square, configures it, and inserts it at index 0
        so existing segments shift forward and the snake grows by one.
        """

        t = Turtle("square")
        t.penup()
        t.color(self.color)
        self.turtles.insert(0, t)

    # Direction control methods ensure the snake cannot instantly reverse

    def down(self):
        """
        Turn head downward unless it's currently moving up."""

        if self.head.heading() != 90:
            self.head.setheading(270)

    def up(self):
        """
        Turn head upward unless it's currently moving down."""

        if self.head.heading() != 270:
            self.head.setheading(90)

    def right(self):
        """
        Turn head right unless it's currently moving left."""

        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        """
        Turn head left unless it's currently moving right."""
        
        if self.head.heading() != 0:
            self.head.setheading(180)
