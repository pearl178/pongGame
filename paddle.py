from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.create(x, y)

    def create(self, x, y):
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.pu()
        self.goto(x, y)
        self.speed('fastest')

    def go_up(self):
        if self.ycor() < 275:
            new_y = self.ycor() + 20
            new_position = (self.xcor(), new_y)
            self.goto(new_position)


    def go_down(self):
        if self.ycor() > -275:
            new_y = self.ycor() - 20
            new_position = (self.xcor(), new_y)
            self.goto(new_position)