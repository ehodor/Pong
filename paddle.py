from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(4, 0.7)
        self.color("white")

    def up(self):
        if self.ycor() <= 290:
            self.goto(x=self.xcor(), y=self.ycor() + 50)

    def down(self):
        if self.ycor() >= -290:
            self.goto(x=self.xcor(), y=self.ycor() - 50)
