from turtle import Turtle

SCORE_XCORD = 0
SCORE_YCORD = 240
FONT = ("Courier", 16, "normal")
ALIGN = "center"
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
        self.high_score = self.get_high_score()
        self.updateScore()

    def updateScore(self):
        '''Updates the current score value and displays it along with the high score'''
        self.clear()
        self.goto(SCORE_XCORD, SCORE_YCORD)
        text = f"High Score: {self.high_score}\nScore: {self.score}"
        self.write(text, True, ALIGN, FONT)
        if self.score > self.high_score:
            self.high_score = self.score
        self.score += 1

    def game_over(self):
        '''Displays game over message'''
        self.goto(END_XCORD, END_YCORD)
        self.write("GAME OVER", True, ALIGN, FONT)

    def get_high_score(self):
        '''Read current high score from text file'''
        with open("high_score.txt", "r") as f:
            val = f.read()
            return int(val)

    def set_high_score(self):
        '''Updated text file with current highest score'''
        with open("high_score.txt", "w") as f:
            f.write(str(self.high_score))
