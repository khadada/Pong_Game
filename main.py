from turtle import Screen
from paddle import Paddle, LEFT_SIDE, RIGHT_SIDE
from ball import Ball
import time
from scoreboard import Score

my_screen = Screen()
my_screen.title("KHALED <3 YASMINE")
my_screen.setup(800, 600)
my_screen.tracer(0)
my_screen.listen()
paddle_left = Paddle(LEFT_SIDE)
paddle_right = Paddle(RIGHT_SIDE)
my_screen.onkey(paddle_right.move_up, 'Up')
my_screen.onkey(paddle_right.move_down, 'Down')
my_screen.onkey(paddle_left.move_up, 'z')
my_screen.onkey(paddle_left.move_down, 's')
ball = Ball()
score = Score()
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -320:
        ball.bounce_y()
    if (ball.distance(paddle_left) < 50 and ball.xcor() < -360) or (ball.distance(paddle_right) < 50 and ball.xcor() > 360):
        ball.bounce_x()
        ball.speed_up()
    elif ball.xcor() < -380:
        score.point_up('right')
        score.update()
        ball.restart()
    elif ball.xcor() > 380:
        score.point_up('left')
        score.update()
        ball.restart()



#    elif ball.distance(paddle_right) < 60 and ball.xcor() < 380:
 #       print('make contact')


my_screen.exitonclick()
