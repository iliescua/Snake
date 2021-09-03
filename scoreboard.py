from turtle import Turtle

SCORE_XCORD = -45
SCORE_YCORD = 270
FONT = ("Courier", 16, "normal")
ALIGN = "left"
END_XCORD = -45
END_YCORD = 0

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("green")
        self.penup()
        self.speed("fastest")
        self.score = 0
        self.updateScore()


    def updateScore(self):
        self.clear()
        self.goto(SCORE_XCORD, SCORE_YCORD)
        self.write(f"Score: {self.score}", True, ALIGN, FONT)
        self.score += 1

    
    def game_over(self):
        self.goto(END_XCORD, END_YCORD)
        self.write("GAME OVER", True, ALIGN, FONT)