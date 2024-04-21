from turtle import Turtle
import random
MOVEMENT=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
RANDOM=random.randint(40,560)
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
        
        
    def create_snake(self):
        for position in STARTING_POSITION:
         self.add_segemnts(position) 
         
          
    def add_segemnts(self,position):
        
            my_turtle=Turtle("square")
            my_turtle.penup()
            my_turtle.color("white")
            my_turtle.goto(position)
            self.segments.append(my_turtle)
            
    def extend(self):
        self.add_segemnts(self.segments[-1].position())
    
    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            
            new_x=self.segments[seg-1].xcor()      #Taking the coordinates of x and y axis
            new_y=self.segments[seg-1].ycor()      
            self.segments[seg].goto(new_x,new_y)    #Moving eachn segments to last of their 
            
        self.head.fd(MOVEMENT) #Moving by 20px
    
    def up(self):
     if self.head.heading !=DOWN:
        self.head.setheading(UP)
    def down(self):
     if self.head.heading !=UP:
        self.head.setheading(DOWN)
    def right(self):
     if self.head.heading !=LEFT:
        self.head.setheading(RIGHT)
    def left(self):
     if self.head.heading !=RIGHT:
        self.head.setheading(LEFT) 
    
        