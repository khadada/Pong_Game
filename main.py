from turtle import Screen
from paddle import Paddle,LEFT_SIDE,RIGHT_SIDE
from ball import Ball

my_screen = Screen()
my_screen.title('Pong game created by Khaled')
my_screen.setup(800, 600)
my_screen.listen()
paddle_left = Paddle(LEFT_SIDE)
paddle_right = Paddle(RIGHT_SIDE)
my_screen.onkey(paddle_right.move_up, 'Up')
my_screen.onkey(paddle_right.move_down, 'Down')
my_screen.onkey(paddle_left.move_up, 'z')
my_screen.onkey(paddle_left.move_down, 's')
ball = Ball()

my_screen.exitonclick()
