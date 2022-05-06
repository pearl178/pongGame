from turtle import Turtle
FONT = ('Courier', 40, 'normal')


class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.color("white")
        self.pu()
        self.hideturtle()
        self.goto(x, y)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", move=False, align='center', font=FONT)

    def game_over(self):
        self.goto(self.x, 0)
        self.color("red")
        self.write("YOU WIN", move=False, align='center', font=FONT)
