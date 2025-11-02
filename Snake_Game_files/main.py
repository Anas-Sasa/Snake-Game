from turtle import Turtle, Screen
from food import Food
from snake import Snake
from scoreborad import Score
import os, time

def clear_terminal():
    os.system("clear" if os.name == "posix" else "cls")

def sleep(seconds):
    time.sleep(seconds)

clear_terminal()

MASSAGE_TURTLE = Food(color= "lavender")

def welcome_screen(window):

    angels = ((-470,330), (-470, -330), (430, 330), (430, -330))

    t = Food(color="lavender")
    t.goto(x= 0, y= 330)
    t.write("Welcome to snack game!🐉 🐉", align= "center", font=("Arial", 20, "normal"))
  
    t.color("green")

    for i in angels:
        t.goto(i)
        t.write("🐉", font=("Arial", 40, "normal"))

    window.update()
    sleep(3)
    t.clear()

def main(): ###########
    global WINDOW

    WINDOW = Screen()
    WINDOW.bgcolor("slate blue")
    WINDOW.title("Anas GB!")
    WINDOW.setup(width= 1000, height= 800)
    WINDOW.tracer(0)

    speed = WINDOW.textinput("Speed of Snake!", "Enter speed of snake from [10] to [20] <<!!! ")

    

    while not speed.isdigit() or int(speed) > 20 or int(speed) < 10:
        
        MASSAGE_TURTLE.write(f"Enter only numbers! [ from 10 to 20 ]", align= "center", font=("Arial", 15, "italic"))
        WINDOW.update()
        sleep(3)
        MASSAGE_TURTLE.clear()
        speed = WINDOW.textinput("Speed of Snake!", "Enter speed of snake from [ 10 to 20 ] <<<||")

    welcome_screen(window= WINDOW)

    food = Food(color= "lime")

    snake = Snake(color= "plum", length= 6, speed= int(speed) )

    score = Score()


    food.apear_food()
    
    game_on = True
    while game_on:

        sleep(0.05)
        score.score_update()

        snake.move(window= WINDOW)

        if snake.head.xcor() > 485 or snake.head.xcor() < -485 or snake.head.ycor() > 385 or snake.head.ycor() < -385:
            game_on = False
            sleep(2)
            snake.hide_snake()
            score.hide_score()
            food.hide_food()
            score.game_over(window= WINDOW)
            
        elif snake.head.distance(food) < 15:

            food.apear_food()
            snake.snake_extend()
            score.score += 1

        else:
            for t in snake.turtles[:-2]:
                if snake.head.distance(t ) <10:

                    game_on = False
                    sleep(2)
                    snake.hide_snake()
                    score.hide_score()
                    food.hide_food()
                    score.game_over(window= WINDOW)
                    


        
        WINDOW.listen()

        WINDOW.onkey(snake.down, "Down")
        WINDOW.onkey(snake.up, "Up")
        WINDOW.onkey(snake.left, "Left")
        WINDOW.onkey(snake.right, "Right")
    
    snake.turtles = []

main()

while True:
    
    new_game = WINDOW.textinput("New Game! ", "Do you want to play again?  Type [ Y ] or Type [ N ] to exit!")
    
    if str(new_game).lower() == "y":

        WINDOW.clear()
        main()
    
    if str(new_game).lower() == 'n':
        break
    
WINDOW.mainloop()