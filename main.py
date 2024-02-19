from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

game_is_on = True

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

ball = Ball()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    ball.check_collision(left_paddle, right_paddle)


screen.exitonclick()
