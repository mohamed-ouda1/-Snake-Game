from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):   
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(.5,.5)
        self.penup()
        self.new_food()

    def new_food(self) :
        x=random.randint(-350,350)
        y=random.randint(-350,350)
        self.goto(x,y)     
        
