from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("circle")
        self.shapesize(1, 1)
        self.color("white")
        self.traj_list = [-3, 3]
        self.x_traj = random.choice(self.traj_list)
        self.y_traj = random.choice(self.traj_list)

    def move(self):
        self.goto(self.xcor()+self.x_traj, self.ycor()+self.y_traj)


    def wall(self):
        if self.y_traj > 0:
            self.y_traj = -3
        else:
            self.y_traj = 3

    def reset(self):
        self.goto(0,0)
        self.x_traj = random.choice(self.traj_list)
        self.y_traj = random.choice(self.traj_list)

