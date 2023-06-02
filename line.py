from turtle import Turtle

class DotLine(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(1, 0.3)
        self.color("white")
        self.penup()

