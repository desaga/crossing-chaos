from turtle import Turtle


class HighWayManager(Turtle):
    def __init__(self, highway_size):
        super().__init__()
        self.number_lines = 8
        self.color("yellow")
        self.highway_size = highway_size
        self.hideturtle()
        self.draw_lanes()

    def draw_lanes(self):
        for i in range(0, self.number_lines):
            self.penup()
            self.setposition(-self.highway_size[0]/2, -200 + i * 400 / self.number_lines)
            for _ in range(0, self.highway_size[1], 10):
                self.pendown()
                self.forward(4)
                self.penup()
                self.forward(7)
            self.pendown()
