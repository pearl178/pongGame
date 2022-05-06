from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
from column import Column


screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor('black')
screen.title("Pong Game")

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
l_scoreboard = Scoreboard(-200, 240)
r_scoreboard = Scoreboard(200, 240)
column = Column()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # Detect miss-catch (right)
    if ball.xcor() > 380:
        ball.reset_position()
        l_scoreboard.score += 1
        l_scoreboard.update_score()

    # Detect miss-catch (left)
    if ball.xcor() < -380:
        ball.reset_position()
        r_scoreboard.score += 1
        r_scoreboard.update_score()

    if l_scoreboard.score == 3:
        l_scoreboard.game_over()
        game_is_on = False

    if r_scoreboard.score == 3:
        r_scoreboard.game_over()
        game_is_on = False


screen.exitonclick()