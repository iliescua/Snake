from turtle import Screen, st
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WIDTH = 600
HEIGHT = 600
HIT_DISTANCE = 15
SLEEP_TIME = 0.1
MAP_END = 290

screen = Screen()
screen.title("Snek")
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.tracer(0)


def start_game():
    screen.reset()
    is_game_on = True
    snake = Snake()
    food = Food()
    sb = Scoreboard()

    screen.listen()
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down, "Down")
    screen.onkeypress(snake.left, "Left")
    screen.onkeypress(snake.right, "Right")
    screen.onkeypress(None, "space")

    while is_game_on:
        screen.update()
        time.sleep(SLEEP_TIME)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < HIT_DISTANCE:
            food.refresh()
            sb.updateScore()
            snake.extend()
        
        # Detect collision with border
        check_pos_x = snake.head.xcor() > MAP_END
        check_neg_x = snake.head.xcor() < -MAP_END
        check_pos_y = snake.head.ycor() > MAP_END
        check_neg_y = snake.head.ycor() < -MAP_END
        
        if check_pos_x or check_neg_x or check_pos_y or check_neg_y:
            snake.border_collision()

        # Detect collision with tail
        for seg in snake.segments[1:]:
            if snake.head.distance(seg) < 10:
                is_game_on = False
                sb.game_over()

    screen.onkeypress(start_game, "space")


start_game()

screen.exitonclick()
