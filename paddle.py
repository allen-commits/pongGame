from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.speed(1)
        self.setposition(position)
        self.shapesize(5, 1)

    def move_up(self):
        new_y = self.ycor() + 35
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 35
        self.goto(self.xcor(), new_y)
