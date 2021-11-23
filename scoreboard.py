from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 280)
        self.player_left_score = 0
        self.player_right_score = 0
        self.hideturtle()
        self.color('black')
        self.print_score()

    def print_score(self):
        self.goto(-100, 280)
        self.write(f'[{self.player_left_score}]   ', False, 'center', ('Courier', 18, 'bold'))
        self.goto(100, 280)
        self.write(f'[{self.player_right_score}] ', False, 'center', ('Courier', 18, 'bold'))

    def update(self):
        self.clear()
        self.print_score()

    def point_up(self, side):
        if side.lower() == "left":
            self.player_left_score += 1
        elif side.lower() == "right":
            self.player_right_score += 1


