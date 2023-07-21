from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.setposition(-0, 220)
        self.update_screen()

    def level_up(self):
        self.score += 1
        self.update_screen()

    def update_screen(self):
        self.clear()
        self.write(f"Level: {self.score}", font=("Arial", 24, "normal"), align="center")

    def game_over(self):
        self.goto(0, 150)
        self.color("red")
        self.write(f"GAME OVER", font=("Arial", 40, "normal"), align="center")