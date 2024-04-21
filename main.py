from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
my_screen=Screen()
my_screen.setup(600,600)
my_screen.bgcolor("black")
my_screen.tracer(0)
scoreboard=Scoreboard()
snake=Snake()  
my_food=Food()
my_screen.listen()
my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.left,"Left")
my_screen.onkey(snake.right,"Right")


game_is_on=True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(my_food)<15:
        my_food.refresh()
        
        snake.extend()
      
        scoreboard.update_score()
    
    if snake.head.xcor() < -280.0 or snake.head.xcor() >280.0 or snake.head.ycor() <-280.0 or snake.head.ycor() >280.0:
        print("You have hit the wall ! Game over!")
        scoreboard.game_over()
        game_is_on=False
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
             game_is_on=False
             scoreboard.game_over()
    
my_screen.exitonclick()
