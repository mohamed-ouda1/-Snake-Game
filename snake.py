from turtle import Turtle
import time
class Snake:
    def __init__(self):
        self.Snake_parts=[]
        self.pos_parts=[(0,0),(-30,0),(-50,0)]
        

    def creat_snake(self):
        for i in range(len(self.pos_parts)):
            part=Turtle("square")
            part.color("white")
            part.penup()
            part.goto(self.pos_parts[i-1]) 
            self.Snake_parts.append(part)
            self.hiad=self.Snake_parts[-1]

    def move_snake(self):
        self.hiad.forward(20)
        
        for i in range(len(self.Snake_parts)-1):
            self.Snake_parts[i].goto(self.Snake_parts[i+1].pos())
 
    def add_part(self):
        new_part=Turtle("square")
        new_part.penup()
        new_part.color("white")
        new_part.goto(self.Snake_parts[0].pos())
        self.Snake_parts.insert(0,new_part)

    
    def move_up(self):  
        self.hiad.setheading(90)             

    def move_left(self):
        self.hiad.setheading(180)  

    def move_Down(self):
        self.hiad.setheading(270)      

    def move_right(self):    
        self.hiad.setheading(360)  