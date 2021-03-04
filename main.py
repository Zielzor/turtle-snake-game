from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Sssnake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # collisions
    if snake.head.distance(food) < 15:
        food.refresh_food()
        score.add_score()
        snake.extend()

    # wall collide
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_on = False
        score.reset_scoreboard()
        snake.reset_snake()

    # tail collision
    for body_part in snake.snake[1:]:
        if snake.head.distance(body_part) < 10:
            # game_on = False
            score.reset_scoreboard()


screen.exitonclick()

