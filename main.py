from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from score import Score

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


is_race_on=True

while is_race_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    #Detect the collision with food.
    if snake.segments[0].distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #Detect the collision with wall.
    if snake.segments[0].xcor()>290 or snake.segments[0].xcor()<-290 or snake.segments[0].ycor()>300 or snake.segments[0].ycor()<-290:
        is_race_on=False
        scoreboard.game_over()
    #Detect collision with the tail.
    for segment in snake.segments:
        if segment==snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) <10:
            is_race_on=False
            scoreboard.game_over()
screen.exitonclick()
