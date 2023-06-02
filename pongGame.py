from turtle import Screen
from paddle import Paddle
from scoreboard import Score
from ball import Ball
from line import DotLine
import time

# creates screen that pops-up
screen = Screen()
first_score = Score()
sec_score = Score()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
play_until = int(screen.numinput("Score Input", "Play until someone reaches what score?"))
line_coord = 310
for i in range(15):
    line = DotLine()
    line.goto(0, line_coord)
    line_coord -= 50

first_player = Paddle()
first_player.goto(x=-320, y=0)
sec_player = Paddle()
sec_player.goto(x=320, y=0)

first_score.goto(-50, 300)
sec_score.goto(50, 300)

first_score.write(f"{first_score.score}", align='center', font=('Courier New', 40, 'normal'))
sec_score.write(f"{sec_score.score}", align='center', font=('Courier New', 40, 'normal'))
ball = Ball()
ball.goto(x=0, y=0)
game_active = True

screen.listen()
screen.onkey(first_player.up, "w")
screen.onkey(first_player.down, "s")
screen.onkey(sec_player.up, "Up")
screen.onkey(sec_player.down, "Down")

while game_active:
    screen.update()
    if first_score.score >= play_until:
        print("First player won!")
        game_active = False
    if sec_score.score >= play_until:
        print("Second player won!")
        game_active = False
    time.sleep(0.01)
    ball.move()
    if ball.ycor() > 340 or ball.ycor() < -330:
        ball.wall()
    if (ball.distance(first_player) < 50 and ball.xcor() < -310) or (ball.distance(sec_player)
                                                                     < 50 and ball.xcor() > 310):
        if ball.x_traj > 0:
            ball.x_traj = -3
        else:
            ball.x_traj = 3

    if ball.xcor() < -330:
        sec_score.increment()
        ball.reset()
    if ball.xcor() > 330:
        first_score.increment()
        ball.reset()

screen.exitonclick()
