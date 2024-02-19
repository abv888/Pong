from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

    def check_collision(self, l_paddle, r_paddle):
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()
        if self.distance(r_paddle) < 50 and self.xcor() > 320 or self.distance(l_paddle) < 50 and self.xcor() < -320:
            self.bounce_x()
        if self.xcor() > 380:
            self.reset_position()
        if self.xcor() < -380:
            self.reset_position()
