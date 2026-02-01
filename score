from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

        self.reset_btn = Turtle()
        self.reset_btn.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def inc(self):
        self.score += 1
        self.update_score()

    def game_over(self, reset_callback):
        self.goto(0, 40)
        self.write("GAME OVER", align=ALIGN, font=FONT)

        # draw reset button
        self.reset_btn.clear()
        self.reset_btn.penup()
        self.reset_btn.goto(0, -20)
        self.reset_btn.color("white")
        self.reset_btn.write("RESET", align=ALIGN, font=("Courier", 20, "bold"))

        self.reset_btn.goto(-50, -40)
        self.reset_btn.showturtle()
        self.reset_btn.shape("square")
        self.reset_btn.shapesize(stretch_wid=1.5, stretch_len=5)
        self.reset_btn.fillcolor("black")
        self.reset_btn.onclick(reset_callback)

    def reset(self):
        self.score = 0
        self.clear()
        self.goto(0, 270)
        self.update_score()
        self.reset_btn.clear()
        self.reset_btn.hideturtle()
