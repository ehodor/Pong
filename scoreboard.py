from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0

    def increment(self):
        self.score+=1
        self.clear()
        self.write(f"{self.score}", align='center', font=('Courier New', 40, 'normal'))