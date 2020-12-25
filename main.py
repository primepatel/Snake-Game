from turtle import Screen
from snake import Snake
from food import Food
from score import Score

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right ")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.05)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extent()
        scoreboard.increase_score()
    if snake.check_head_on_wall():
        scoreboard.game_over()
        is_game_on = False
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            is_game_on = False
            scoreboard.game_over()
screen.exitonclick()
