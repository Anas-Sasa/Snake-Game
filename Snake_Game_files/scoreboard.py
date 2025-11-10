from turtle import Turtle
import time


class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.color("violet")
        self.goto(x= 0, y= 350)
        self.score = 0

    def score_update(self):
        self.clear()
        self.write(f"Game score: {self.score}", align= "center", font=("Arial", 25, "normal"))
        
    def game_over(self, window):

        self.goto(x= 0, y= 0)
        window.bgcolor("crimson")
        self.color("peach puff")
        self.write(f"Game over!🥲 😔 💔\n\nLaste score: {self.score} ", align= "center", font=("Arial", 20, "italic"))

        angels = ((-470,330), (-470, -330), (430, 330), (430, -330))


        for i in angels:
            self.goto(i)
            self.write("🐉", font=("Arial", 40, "normal"))
        window.update()
        time.sleep(2)
    
    def hide_score(self):
        self.clear()