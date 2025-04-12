import time
from turtle import Turtle , Screen
from snake import Snake
from score import Score
from food import Food
screen=Screen()
screen.setup(800,800)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
snake=Snake()
score=Score()
snake.creat_snake()
food=Food()
game_on=True

while game_on:
    snake.move_snake()
    
    screen.update()
    time.sleep(.1)
    score.score_pord()
    screen.listen()
    screen.onkey(snake.move_up,"Up")
    screen.onkey(snake.move_Down,"Down")
    screen.onkey(snake.move_left,"Left")
    screen.onkey(snake.move_right,"Right")
    
    

    if snake.hiad.distance(food)<15: 
        score.updat()
        food.new_food()
        snake.add_part()

    if snake.hiad.ycor()>380 or snake.hiad.ycor() <-380 or snake.hiad.xcor()>380 or snake.hiad.xcor()<-380 :
        score.game_over()
        game_on=False
    
    for m in snake.Snake_parts[:-2]:
        if snake.hiad.distance(m) < 10:
            score.game_over() 
            game_on=False
    





















screen.exitonclick()
