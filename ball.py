from turtle import Turtle

class Ball (Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('black')
        self.penup()
        self.goto(0, 0)
        self.move_x = 3
        self.move_y = 4

    def move(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1

    def restart(self):
        self.goto(0, 0)
        self.bounce_x()