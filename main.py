from turtle import Turtle, Screen
import time

# Screen set up
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("The Snake Game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    snake = Turtle()
    snake.color("white")
    snake.shape("square")
    snake.penup()
    snake.goto(position)
    segments.append(snake)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.2)

    for segment in range(len(segments) - 1, 0, -1):
        new_x = segments[segment - 1].xcor()
        new_y = segments[segment - 1].ycor()
        segments[segment].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)

screen.exitonclick()















