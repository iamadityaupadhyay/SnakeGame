from food import Food
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.update_score()
        self.hideturtle()
    def display(self):
        # self.write(f"Aditya's Score is 1 Lacs. How much yours?")
        # self.goto(-270,270)
        self.write(f"Score : {(self.score)-1}", align="center",font=["Arial",16,"normal"])
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align="center",font=("Arial",25,"normal"))
    def update_score(self):
        self.goto(0,270)
        self.clear()
        self.score+=1
        
        self.display()