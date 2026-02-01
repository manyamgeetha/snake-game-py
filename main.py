import time
from turtle import Screen
from sn2 import Snake
from sn3 import Food
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

def reset_game(x=None, y=None):
    global game_on
    score.clear()
    score.reset()
    snake.reset()
    food.refresh()
    game_on = True

while True:
    screen.update()
    time.sleep(0.1)

    if game_on:
        snake.move()

        # food collision
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.inc()

        # wall collision
        if (
            snake.head.xcor() > 280 or snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or snake.head.ycor() < -280
        ):
            game_on = False
            score.game_over(reset_game)

        # tail collision
        for seg in snake.segs[1:]:
            if snake.head.distance(seg) < 10:
                game_on = False
                score.game_over(reset_game)

screen.exitonclick()
