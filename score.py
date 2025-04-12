from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.sco=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,360)
        

    def score_pord(self):
        self.write(f"Score: {self.sco} ", align="center",font=("Arial",24,"normal"))

    def game_over(self):
        self.color("red")
        self.hideturtle()
        self.penup()
        self.goto(0,0)
        self.write(f"game over ", align="center",font=("Arial",40,"normal"))

    def updat(self):
        self.sco +=1
        self.clear()
        self.score_pord()
