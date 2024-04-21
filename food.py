from snake import Snake
from turtle import Turtle
import random
import time

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.speed("fastest")
        self.color("red")
        
        self.refresh()
    def refresh(self):
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        self.goto(x,y)
        
          