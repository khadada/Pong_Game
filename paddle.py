from turtle import Turtle
LEFT_SIDE = -380
RIGHT_SIDE = 380
class Paddle(Turtle):
    def __init__(self,side):
        super().__init__()
        self.shape('square')
        self.color("black")
        self.penup()
        self.shapesize(5, 1)
        self.setx(side)

    def move_up(self):
        if self.ycor() < 290:
            self.goto(self.xcor(), self.ycor()+20)

    def move_down(self):
        if self.ycor() > -290:
            self.goto(self.xcor(), self.ycor()-20)
