from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

# Screen set up
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()


screen.listen()
screen.onkey(snake.right, 'Right')
screen.onkey(snake.up, 'Up')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.down, 'Down')


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.food_position()
        score_board.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.game_over()

screen.exitonclick()
